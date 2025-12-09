import sys
from pathlib import Path

# Add utils to path  
sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.solution_template import Solution

class Day09(Solution):
    def __init__(self):
        super().__init__(day=9)
        
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
        max_area = 0
        red_tiles = []
        for line in data:
            x, y = map(int, line.split(','))
            red_tiles.append((x, y))
        
        n = len(red_tiles)
        
        for i in range(n):
            x1, y1 = red_tiles[i]
            for j in range(i + 1, n):
                x2, y2 = red_tiles[j]
                
                if x1 != x2 and y1 != y2:
                    w = abs(x1 - x2) + 1
                    h = abs(y1 - y2) + 1
                    area = w * h
                    
                    if area > max_area:
                        max_area = area
        return max_area
    
    def part2(self, data):
        red_tiles = []
        for line in data:
            x, y = map(int, line.split(','))
            red_tiles.append((x, y))
        
        # Step 1: Build boundaries dictionary
        boundaries = {}  # y -> [min_x, max_x]
        
        n = len(red_tiles)
        for i in range(n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[(i + 1) % n]  # Wrap around
            
            if x1 == x2:  # Vertical edge
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    if y not in boundaries:
                        boundaries[y] = [x1, x1]
                    else:
                        boundaries[y][0] = min(boundaries[y][0], x1)
                        boundaries[y][1] = max(boundaries[y][1], x1)
            
            else:  # y1 == y2, Horizontal edge
                y = y1
                if y not in boundaries:
                    boundaries[y] = [min(x1, x2), max(x1, x2)]
                else:
                    boundaries[y][0] = min(boundaries[y][0], x1, x2)
                    boundaries[y][1] = max(boundaries[y][1], x1, x2)
        
        # Step 2: Check all pairs of red tiles
        max_area = 0
        for i in range(n):
            x1, y1 = red_tiles[i]
            for j in range(i + 1, n):
                x2, y2 = red_tiles[j]
                
                # Must be opposite corners
                if x1 == x2 or y1 == y2:
                    continue
                
                # Get rectangle bounds
                left = min(x1, x2)
                right = max(x1, x2)
                top = min(y1, y2)
                bottom = max(y1, y2)
                
                # Check if rectangle fits within boundaries
                valid = True
                for y in range(top, bottom + 1):
                    if y not in boundaries:
                        valid = False
                        break
                    bound_left, bound_right = boundaries[y]
                    if left < bound_left or right > bound_right:
                        valid = False
                        break
                    
                if valid:
                    width = right - left + 1
                    height = bottom - top + 1
                    area = width * height
                    if area > max_area:
                        max_area = area
        
        return max_area        
        
    def run(self):
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        import argparse
        parser = argparse.ArgumentParser(description=f'Run Day 9 solutions')
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
            print(f"--- Day 09 Test Cases ---")
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
    solution = Day09()
    solution.run()
