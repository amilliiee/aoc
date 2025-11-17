import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

from utils.solution_template import Solution

class Day03(Solution):
    def __init__(self):
        super().__init__(day=3)
        
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
        # Find number of houses visited
        # Don't care about number of visits to each house, just unique houses
        visited = set()
        visited.add((0, 0)) # Start position
        x, y = 0, 0
        
        for direction in data:
            match direction:
                case '<':
                    x -= 1
                case '>':
                    x += 1
                case 'v':
                    y -= 1
                case '^':
                    y += 1
                case _:
                    print(f"{direction} is not a valid direction")
            visited.add((x, y))
        return len(visited)
    
    def part2(self, data):
        # Find number of houses that receive at least one present
        # Santa and Robo-Santa take turns moving
        visited = set()
        visited.add((0, 0)) # Start position
        positions = [[0, 0], [0, 0]] # Santa, Robo-Santa
        
        for i, direction in enumerate(data):
            curr_turn = i % 2
            match direction:
                case '<':
                    positions[curr_turn][0] -= 1
                case '>':
                    positions[curr_turn][0] += 1
                case 'v':
                    positions[curr_turn][1] -= 1
                case '^':
                    positions[curr_turn][1] += 1
                case _:
                    print(f"{direction} is not a valid direction")
            visited.add((positions[curr_turn][0], positions[curr_turn][1]))
        return len(visited)
        
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
    solution = Day03()
    solution.run()
