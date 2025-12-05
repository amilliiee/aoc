import sys
from pathlib import Path

# Add utils to path  
sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.solution_template import Solution

class Day05(Solution):
    def __init__(self):
        super().__init__(day=5)
        
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
        empty_idx = data.index('')
        ranges = data[:empty_idx]
        ids = data[empty_idx + 1:]
        valid_ids = 0
        
        for id in ids:
            for range_str in ranges:
                nums = range_str.split('-')
                low = int(nums[0])
                high = int(nums[1])
                val = int(id)
                if low <= val <= high:
                    valid_ids += 1
                    break
        return valid_ids
        
    
    def part2(self, data):
        empty_idx = data.index('')
        ranges = data[:empty_idx]
        r = []
        
        for range_str in ranges:
            nums = range_str.split('-')
            low = int(nums[0])
            high = int(nums[1])
            r.append((low, high))
        
        sorted_ranges = sorted(r)
        merged = [sorted_ranges[0]]
        for curr_start, curr_end in sorted_ranges[1:]:
            last_start, last_end = merged[-1]
            if curr_start <= last_end + 1:
                merged[-1] = (last_start, max(last_end, curr_end))
            else:
                merged.append((curr_start, curr_end))
        
        tot = 0
        for tup in merged:
            tot += tup[1] - tup[0] + 1
        return tot
        
    def run(self):
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        import argparse
        parser = argparse.ArgumentParser(description=f'Run Day 5 solutions')
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
            print(f"--- Day 05 Test Cases ---")
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
    solution = Day05()
    solution.run()
