import sys
from pathlib import Path

# Add utils to path  
sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.solution_template import Solution

class Day01(Solution):
    def __init__(self):
        super().__init__(day=1)
        
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
            #return f.read().strip() # Use for char by char reading inside part1/2
            return [line.strip() for line in f] # Use for line by line reading inside part1/2
    
    def read_input(self, test=False):
        # Read input file
        filename = "test.txt" if test else "input.txt"
        filepath = Path(__file__).parent / filename
        
        with open(filepath, 'r') as f:
            #return f.read().strip() # Use for char by char reading inside part1/2
            return [line.strip() for line in f] # Use for line by line reading inside part1/2
    
    def part1(self, data):
        zero_ct = 0
        pos = 50
        
        for line in data:
            dir = line[0]
            dist = int(line[1:])
            if dir.upper() == 'L':
                pos = (pos - dist) % 100
            else:
                pos = (pos + dist) % 100
            if pos == 0:
                zero_ct += 1
        return zero_ct
    
    def part2(self, data):
        zero_ct = 0
        pos = 50

        for line in enumerate(data, 1):
            dir = line[0]
            dist = int(line[1:])

            if dir.upper() == 'L':
                # Count zeros during left turn
                for step in range(1, dist + 1):
                    if (pos - step) % 100 == 0:
                        zero_ct += 1
                pos = (pos - dist) % 100
            else:  # 'R'
                # Count zeros during right turn  
                for step in range(1, dist + 1):
                    if (pos + step) % 100 == 0:
                        zero_ct += 1
                pos = (pos + dist) % 100
        return zero_ct
        
    def run(self):
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        import argparse
        parser = argparse.ArgumentParser(description=f'Run Day 1 solutions')
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
            print(f"--- Day 01 Test Cases ---")
            for i, test_input in enumerate(self.test_inputs, 1):
                if not args.part or args.part == 1:
                    result1 = self.part1([test_input])
                    print(f"Part 1 Test {i}: '{test_input}' -> {result1}")
                if not args.part or args.part == 2:
                    try:
                        result2 = self.part2([test_input])
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
    solution = Day01()
    solution.run()
