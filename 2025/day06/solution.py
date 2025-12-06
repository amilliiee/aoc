import sys
from pathlib import Path

# Add utils to path  
sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.solution_template import Solution

class Day06(Solution):
    def __init__(self):
        super().__init__(day=6)
        
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
            #return f.read().strip() # Use for char by char reading inside part1/2
            return [line.strip() for line in f] # Use for line by line reading inside part1/2
    
    def part1(self, data):
        tot = 0
        lines = data
        max_len = max(len(line) for line in lines)
        grid = [list(line.ljust(max_len)) for line in lines]
        
        separators = []
        for col in range(max_len):
            if all(grid[row][col] == ' ' for row in range(len(grid))):
                separators.append(col)
        
        prev_sep = -1
        for sep in separators + [max_len]:
            if sep - prev_sep > 1:
                prob_cols = range(prev_sep + 1, sep)
                vals = []
                for row in range(len(grid) - 1):
                    chars = []
                    for col in prob_cols:
                        ch = grid[row][col]
                        if ch != ' ':
                            chars.append(ch)
                    if chars:
                        n = int(''.join(chars))
                        vals.append(n)
                        
                op_chars = []
                for col in prob_cols:
                    ch = grid[-1][col]
                    if ch != ' ':
                        op_chars.append(ch)
                operator = op_chars[0] if op_chars else None
                if operator == '+':
                    result = sum(vals)
                elif operator == '*':
                    result = 1
                    for val in vals:
                        result *= val
                tot += result
            prev_sep = sep
        return tot
    
    def part2(self, data):
        tot = 0
        lines = data
        max_len = max(len(line) for line in lines)
        grid = [list(line.ljust(max_len)) for line in lines]
        
        separators = []
        for col in range(max_len):
            if all(grid[row][col] == ' ' for row in range(len(grid))):
                separators.append(col)
        
        prev_sep = -1
        for sep in separators + [max_len]:
            if sep - prev_sep > 1:
                prob_cols = range(prev_sep + 1, sep)
                vals = []
                for col in prob_cols:
                    digits = []
                    for row in range(len(grid) - 1):
                        ch = grid[row][col]
                        if ch != ' ':
                            digits.append(ch)
                    if digits:
                        n = int(''.join(digits))
                        vals.append(n)
                        
                op_chars = []
                for col in prob_cols:
                    ch = grid[-1][col]
                    if ch != ' ':
                        op_chars.append(ch)
                operator = op_chars[0] if op_chars else None
                if operator == '+':
                    result = sum(vals)
                elif operator == '*':
                    result = 1
                    for val in vals:
                        result *= val
                tot += result
            prev_sep = sep
        return tot
        
        
    def run(self):
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        import argparse
        parser = argparse.ArgumentParser(description=f'Run Day 6 solutions')
        parser.add_argument('--part', type=int, choices=[1, 2], help='Run specific part')
        parser.add_argument('--test', action='store_true', help='Run tests only')
        parser.add_argument('--real', action='store_true', help='Run real data only')
        
        # Parse command line args if any, else use defaults
        try:
            args = parser.parse_args()
        except SystemExit:
            args = argparse.Namespace(part=None, test=False, real=False)
        
        if not args.real:
            # Run tests
            print(f"--- Day 06 Test Cases ---")
            for i, test_input in enumerate(self.test_inputs, 1):
                if not args.part or args.part == 1:
                    result1 = self.part1([test_input] if self.day >= 9 else test_input)
                    print(f"Part 1 Test {i}: '{test_input}' -> {result1}")
                if not args.part or args.part == 2:
                    try:
                        result2 = self.part2([test_input] if self.day >= 9 else test_input)
                        print(f"Part 2 Test {i}: '{test_input}' -> {result2}")
                    except Exception as e:
                        print(f"Part 2 Test {i}: Not implemented - {e}")
            print()
        
        if not args.test:
            # Run real data
            print("--- Real Data ---")
            if not args.part or args.part == 1:
                real_result1 = self.part1(self.real_data)
                print(f"Part 1: {real_result1}")
            if not args.part or args.part == 2:
                try:
                    real_result2 = self.part2(self.real_data)
                    print(f"Part 2: {real_result2}")
                except Exception as e:
                    print(f"Part 2 not implemented: {e}")

if __name__ == "__main__":
    solution = Day06()
    solution.run()
