import sys
from pathlib import Path

# Add utils to path  
sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.solution_template import Solution

class Day12(Solution):
    def __init__(self):
        super().__init__(day=12)
        
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
        # Join all lines and split by double newline
        text = '\n'.join(data)
        
        # The input has shapes separated by blank lines, then regions
        parts = text.strip().split('\n\n')
        
        # Last part is regions
        regions_text = parts[-1]
        
        # All parts before last are shapes
        shapes_text = '\n\n'.join(parts[:-1])
        
        # Count # in each shape (shapes are separated by blank lines)
        shapes = shapes_text.strip().split('\n\n')
        shapes_hash_counts = [shape.count('#') for shape in shapes]
        
        # Process regions
        count_fitting = 0
        for line in regions_text.strip().split('\n'):
            if ':' not in line:
                continue
                
            size_part, counts_part = line.split(':')
            w, h = map(int, size_part.split('x'))
            counts = list(map(int, counts_part.split()))
            
            # Calculate total # cells needed
            total_hash = 0
            for i, count in enumerate(counts):
                if i < len(shapes_hash_counts):
                    total_hash += count * shapes_hash_counts[i]
            
            area = w * h
            
            # The cheat others found: if total_hash <= area, it fits
            if total_hash <= area:
                count_fitting += 1
        
        return count_fitting
    
    def part2(self, data):
        # Solution for part 2
        # Your implementation here
        return None
        
    def run(self):
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        import argparse
        parser = argparse.ArgumentParser(description=f'Run Day 12 solutions')
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
            print(f"--- Day 12 Test Cases ---")
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
    solution = Day12()
    solution.run()
