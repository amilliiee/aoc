import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.solution_template import Solution

class Day07(Solution):
    def __init__(self):
        super().__init__(day=7)
        
    def load_data(self):
        # Override to handle test cases differently
        self.test_inputs = self.read_test_inputs()
        self.real_data = self.read_input(test=False)
        return self
    
    def read_test_inputs(self):
        # Read test inputs from file with comments
        filepath = Path(__file__).parent / "test.txt"
        test_inputs = []
        
        with open(filepath, 'r') as f:
            for line in f:
                clean_line = line.strip()
                if clean_line and not clean_line.startswith('#'):
                    test_inputs.append(clean_line)
        return test_inputs
    
    def read_input(self, test=False):
        # Read input file
        filename = "test.txt" if test else "input.txt"
        filepath = Path(__file__).parent / filename
        
        with open(filepath, 'r') as f:
            return [line.strip() for line in f]
    
    def part1(self, data):
        # Determine signal provided to wire a
        instructions = {}
        
        for line in data:
            if ' -> ' not in line:
                continue
            op, wire = line.split(' -> ') # Gather instructions and output wire
            parts = op.split() # Gather individual parts of instructions
            
            if len(parts) == 1:
                # '123 -> x' or 'ab -> cd'
                instructions[wire] = ('DIRECT', parts[0])
            elif len(parts) == 2:
                # 'NOT c -> d'
                instructions[wire] = (parts[0], parts[1])
            elif len(parts) == 3:
                # 'mn AND mp -> np' or 'hb OR hc -> hd' or 'eo LSHIFT (or RSHIFT) 12 -> fo'
                instructions[wire] = (parts[1], parts[0], parts[2])
        
        cache = {}
        def evaluate(wire):
            if wire in cache:
                return cache[wire]
            
            if wire.isdigit():
                result = int(wire)
            else:
                ins = instructions[wire]
                op = ins[0]
            
                # Recursively evaluate the operands until you get an integer
                if op == 'DIRECT':
                    result = evaluate(ins[1]) & 0xFFFF
                elif op == 'NOT':
                    result = ~evaluate(ins[1]) & 0xFFFF
                elif op == 'AND':
                    result = (evaluate(ins[1]) & evaluate(ins[2])) & 0xFFFF
                elif op == 'OR':
                    result = (evaluate(ins[1]) | evaluate(ins[2])) & 0xFFFF
                # Not recursively evaluating the shift amount as it's always a number
                elif op == 'RSHIFT':
                    result = (evaluate(ins[1]) >> int(ins[2])) & 0xFFFF
                elif op == 'LSHIFT':
                    result = (evaluate(ins[1]) << int(ins[2])) & 0xFFFF
            cache[wire] = result
            return result
        return evaluate('a')
    
    def part2(self, data):
        # Same evaluation, but take the answer for part 1 and make that the numerical value for b, then reevaluate
        # Determine signal provided to wire a
        # Chose to just copy paste since this is a challenge for AoC. In actual production the evaluation method would be turned into a class method
        # Determine signal provided to wire a
        instructions = {}
        
        for line in data:
            if ' -> ' not in line:
                continue
            op, wire = line.split(' -> ') # Gather instructions and output wire
            parts = op.split() # Gather individual parts of instructions
            
            if len(parts) == 1:
                # '123 -> x' or 'ab -> cd'
                instructions[wire] = ('DIRECT', parts[0])
            elif len(parts) == 2:
                # 'NOT c -> d'
                instructions[wire] = (parts[0], parts[1])
            elif len(parts) == 3:
                # 'mn AND mp -> np' or 'hb OR hc -> hd' or 'eo LSHIFT (or RSHIFT) 12 -> fo'
                instructions[wire] = (parts[1], parts[0], parts[2])
        
        cache = {}
        def evaluate(wire):
            if wire in cache:
                return cache[wire]
            
            if wire.isdigit():
                result = int(wire)
            else:
                ins = instructions[wire]
                op = ins[0]
            
                # Recursively evaluate the operands until you get an integer
                if op == 'DIRECT':
                    result = evaluate(ins[1]) & 0xFFFF
                elif op == 'NOT':
                    result = ~evaluate(ins[1]) & 0xFFFF
                elif op == 'AND':
                    result = (evaluate(ins[1]) & evaluate(ins[2])) & 0xFFFF
                elif op == 'OR':
                    result = (evaluate(ins[1]) | evaluate(ins[2])) & 0xFFFF
                # Not recursively evaluating the shift amount as it's always a number
                elif op == 'RSHIFT':
                    result = (evaluate(ins[1]) >> int(ins[2])) & 0xFFFF
                elif op == 'LSHIFT':
                    result = (evaluate(ins[1]) << int(ins[2])) & 0xFFFF
            cache[wire] = result
            return result
        instructions['b'] = ('DIRECT', str(evaluate('a')))
        cache.clear()
        return evaluate('a')
        
    def run_tests(self):
        # Run all test cases with expected results
        print(f"--- Day {self.day:02d} Test Cases ---")
        for i, test_input in enumerate(self.test_inputs, 1):
            result = self.part1(test_input)
            print(f"Test {i}: '{test_input}' -> {result}")
    
    def run(self):
        # Run both parts with test and real data
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        # Run individual test cases
        #self.run_tests()
        #print()
        
        # Run on real data
        print("--- Real Data ---")
        real_result1 = self.part1(self.real_data)
        print(f"Part 1: {real_result1}")
        
        try:
            real_result2 = self.part2(self.real_data)
            print(f"Part 2: {real_result2}")
        except Exception as e:
            print(f"Part 2 not implemented: {e}")

if __name__ == "__main__":
    solution = Day07()
    solution.run()
