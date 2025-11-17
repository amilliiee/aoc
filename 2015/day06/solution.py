import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

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
            return [line.strip() for line in f]
    
    def part1(self, data):
        # Turn on/off lights in 1000x1000 grid, then count how manny are on at the end
        lights = [[0] * 1000 for _ in range(1000)]
        
        for line in data:
            parts = line.split()
            if line.startswith('turn on') or line.startswith('turn off'):
                [a, b] = map(int, parts[2].split(','))
                [x, y] = map(int, parts[4].split(','))
            elif line.startswith('toggle'):
                [a, b] = map(int, parts[1].split(','))
                [x, y] = map(int, parts[3].split(','))
            
            for row in range(b, y + 1):
                for col in range(a, x + 1):
                    if line.startswith('turn on'):
                        lights[row][col] = 1
                    elif line.startswith('turn off'):
                        lights[row][col] = 0
                    elif line.startswith('toggle'):
                        lights[row][col] = 1 - lights[row][col]
        
        total = 0
        for row in lights:
            total += sum(row)
        return total
    
    def part2(self, data):
        # Turn on: +1, turn off: -1, toggle: +2
        lights = [[0] * 1000 for _ in range(1000)]
        
        for line in data:
            parts = line.split()
            if line.startswith('turn on') or line.startswith('turn off'):
                [a, b] = map(int, parts[2].split(','))
                [x, y] = map(int, parts[4].split(','))
            elif line.startswith('toggle'):
                [a, b] = map(int, parts[1].split(','))
                [x, y] = map(int, parts[3].split(','))
            
            for row in range(b, y + 1):
                for col in range(a, x + 1):
                    if line.startswith('turn on'):
                        lights[row][col] += 1
                    elif line.startswith('turn off'):
                        lights[row][col] = max(0, lights[row][col] - 1)
                    elif line.startswith('toggle'):
                        lights[row][col] += 2
        
        total = 0
        for row in lights:
            total += sum(row)
        return total
        
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
        self.run_tests()
        print()
        
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
    solution = Day06()
    solution.run()
