import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.solution_template import Solution

class Day02(Solution):
    def __init__(self):
        super().__init__(day=2)
        
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
            return f.read().strip()
    
    def part1(self, data):
        # Find wrapping paper required to wrap all presents
        # Wrapping paper per present = 2*l*w + 2*w*h + 2*l*h + area of smallest side
        total = 0
        
        if isinstance(data, str):
            lines = data.splitlines()
        else:
            lines = data
            
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = line.split('x')
            if len(parts) != 3:
                continue
            
            l, w, h = map(int, line.split('x'))
            areas = [l*w, l*h, w*h]
            total += 2 * sum(areas) + min(areas)
        return total
    
    def part2(self, data):
        # Find ribbon needed for each present
        # Ribbon per present = smallest perimeter + volume of present
        total = 0
        
        if isinstance(data, str):
            lines = data.splitlines()
        else:
            lines = data
            
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = line.split('x')
            if len(parts) != 3:
                continue
            
            l, w, h = map(int, line.split('x'))
            perims = [2*l+2*w, 2*l+2*h, 2*w+2*h]
            vol = l*w*h
            total += min(perims) + vol
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
    solution = Day02()
    solution.run()
