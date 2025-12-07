import sys
from pathlib import Path

# Add utils to path  
sys.path.append(str(Path(__file__).parent.parent.parent))

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
            #return f.read().strip() # Use for char by char reading inside part1/2
            return [line.strip() for line in f] # Use for line by line reading inside part1/2
    
    def part1(self, data):
        grid = [list(line) for line in data]
        rows, cols = len(grid), len(grid[0])
        
        # Find start 'S'
        start_c = grid[0].index('S')
        
        queue = [(1, start_c)]
        visited = set()
        split_ct = 0
        
        while queue:
            r, c = queue.pop(0)
            
            if not (0 <= r < rows and 0 <= c < cols):
                continue
            if (r, c) in visited:
                continue
            
            visited.add((r, c))
            
            if grid[r][c] == '^':
                split_ct += 1
                if c > 0:
                    queue.append((r + 1, c - 1))
                if c < cols - 1:
                    queue.append((r + 1, c + 1))
            elif grid[r][c] == '.':
                queue.append((r + 1, c))
        return split_ct
    
    def part2(self, data):
        grid = [list(line) for line in data]
        rows, cols = len(grid), len(grid[0])
        start_c = grid[0].index('S')
        memo = {}
        
        def ct_tls(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            if r >= rows or c < 0 or c >= cols:
                memo[(r, c)] = 1
                return 1
            
            if grid[r][c] == '^':
                left = ct_tls(r + 1, c - 1)
                right = ct_tls(r + 1, c + 1)
                rslt = left + right
                memo[(r, c)] = rslt
                return rslt
            
            rslt = ct_tls(r + 1, c)
            memo[(r, c)] = rslt
            return rslt
        
        return ct_tls(1, start_c)
        
    def run(self):
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        import argparse
        parser = argparse.ArgumentParser(description=f'Run Day 7 solutions')
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
            print(f"--- Day 07 Test Cases ---")
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
    solution = Day07()
    solution.run()
