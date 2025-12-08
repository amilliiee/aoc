import sys
from pathlib import Path

# Add utils to path  
sys.path.append(str(Path(__file__).parent.parent.parent))

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
            #return f.read().strip() # Use for char by char reading inside part1/2
            return [line.strip() for line in f] # Use for line by line reading inside part1/2
    
    def part1(self, data):
        pts = []
        for line in data:
            x, y, z = map(int, line.split(','))
            pts.append((x, y, z))
        
        n = len(pts)
        parent = list(range(n))
        size = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False # Same root, already connected
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            return True
        
        pairs = []
        for i in range(n):
            xi, yi, zi = pts[i]
            for j in range(i + 1, n):
                xj, yj, zj = pts[j]
                dx = xi - xj
                dy = yi - yj
                dz = zi - zj
                dist_sq = dx*dx + dy*dy + dz*dz
                pairs.append((dist_sq, i, j))
        
        pairs.sort()
        
        for idx, (dist_sq, i, j) in enumerate(pairs):
            union(i, j)
            if idx + 1 == 1000:
                break
        
        circ_sizes = []
        for i in range(n):
            if parent[i] == i:
                circ_sizes.append(size[i])
        
        circ_sizes.sort(reverse=True)
        if len(circ_sizes) >= 3:
            return circ_sizes[0] * circ_sizes[1] * circ_sizes[2]
        else:
            result = 1
            for size in circ_sizes:
                result *= size
            return result
    
    def part2(self, data):
        pts = []
        for line in data:
            x, y, z = map(int, line.split(','))
            pts.append((x, y, z))
        
        n = len(pts)
        parent = list(range(n))
        size = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False # Same root, already connected
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            return True
        
        pairs = []
        for i in range(n):
            xi, yi, zi = pts[i]
            for j in range(i + 1, n):
                xj, yj, zj = pts[j]
                dx = xi - xj
                dy = yi - yj
                dz = zi - zj
                dist_sq = dx*dx + dy*dy + dz*dz
                pairs.append((dist_sq, i, j))
        
        pairs.sort()
        
        circ_ct = n
        for dist_sq, i, j in pairs:
            if union(i, j):
                circ_ct -= 1
                if circ_ct == 1:
                    x1 = pts[i][0]
                    x2 = pts[j][0]
                    return x1 * x2
        
    def run(self):
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        import argparse
        parser = argparse.ArgumentParser(description=f'Run Day 8 solutions')
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
            print(f"--- Day 08 Test Cases ---")
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
    solution = Day08()
    solution.run()
