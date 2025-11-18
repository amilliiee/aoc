import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.solution_template import Solution

class Day08(Solution):
    def __init__(self):
        super().__init__(day=8)
        
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
        code_len = 0
        mem_len = 0
        for line in data:
            code_len += len(line)
            
            # Calculate memory length of line
            stripped = line[1:-1] # Removes surrounding quotes
            i = 0
            line_mem = 0
            while i < len(stripped):
                if stripped[i] == '\\':
                    # Handle escape sequences
                    if stripped[i+1] in ['\\', '"']:
                        line_mem += 1
                        i += 2
                    elif stripped[i+1] == 'x':
                        line_mem += 1
                        i += 4
                else:
                    line_mem += 1
                    i += 1
            mem_len += line_mem
        return code_len - mem_len
    
    def part2(self, data):
        # The reverse of part 1, now encode the strings
        code_len = 0
        mem_len = 0
        for line in data:
            mem_len += len(line)
            
            # Calculate encoded length of line
            encoded = '"'
            for char in line:
                if char == '\\':        # single \
                    encoded += '\\\\'   # double \
                elif char == '"':
                    encoded += '\\"'
                else:
                    encoded += char
            encoded += '"'
            code_len += len(encoded)
        return code_len - mem_len
        
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
    solution = Day08()
    solution.run()
