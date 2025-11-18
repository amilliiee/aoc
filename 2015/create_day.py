from pathlib import Path
import sys

def create_day(day):
    # Create template files for a new day
    day_str = f"day{day:02d}"
    day_dir = Path(day_str)
    day_dir.mkdir(exist_ok=True)
    
    # Create solution.py template
    solution_template = f'''import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.solution_template import Solution

class Day{day:02d}(Solution):
    def __init__(self):
        super().__init__(day={day})
        
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
            return f.read().strip() # Use for char by char reading inside part1/2
            # return [line.strip() for line in f] # Use for line by line reading inside part1/2
    
    def part1(self, data):
        # Solution for part 1
        # Your implementation here
        return None
    
    def part2(self, data):
        # Solution for part 2
        # Your implementation here
        return None
        
    def run_tests(self):
        # Run all test cases with expected results
        print(f"--- Day {{self.day:02d}} Test Cases ---")
        for i, test_input in enumerate(self.test_inputs, 1):
            result = self.part1(test_input)
            print(f"Test {{i}}: '{{test_input}}' -> {{result}}")
    
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
        print(f"Part 1: {{real_result1}}")
        
        try:
            real_result2 = self.part2(self.real_data)
            print(f"Part 2: {{real_result2}}")
        except Exception as e:
            print(f"Part 2 not implemented: {{e}}")

if __name__ == "__main__":
    solution = Day{day:02d}()
    solution.run()
'''
    
    (day_dir / "solution.py").write_text(solution_template)
    (day_dir / "input.txt").touch()
    (day_dir / "test.txt").touch()
    
    print(f"Created {day_str}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        day = int(sys.argv[1])
        create_day(day)
    else:
        print("Usage: python create_day.py <day_number>")