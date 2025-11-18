import sys
from pathlib import Path
from itertools import permutations as p

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

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
            return [line.strip() for line in f]
    
    def part1(self, data):
        # Find the shortest route that visits all cities
        cities = set()
        distances = {}
        for line in data:
            ins = line.split()
            city1, city2 = ins[0], ins[2] # Input always in the form of CITY to CITY = DISTANCE
            cities.add(city1)
            cities.add(city2)
            distances[(city1, city2)] = distances[(city2, city1)] = int(ins[4])
        
        min_dist = float('inf')
        for route in p(cities):
            total = 0
            for i in range(len(route) - 1):
                total += distances[(route[i], route[i+1])]
            min_dist = min(min_dist, total)
        return min_dist
    
    def part2(self, data):
        # Find the longest route that visits all cities
        cities = set()
        distances = {}
        for line in data:
            ins = line.split()
            city1, city2 = ins[0], ins[2] # Input always in the form of CITY to CITY = DISTANCE
            cities.add(city1)
            cities.add(city2)
            distances[(city1, city2)] = distances[(city2, city1)] = int(ins[4])
        
        max_dist = float('-inf')
        for route in p(cities):
            total = 0
            for i in range(len(route) - 1):
                total += distances[(route[i], route[i+1])]
            max_dist = max(max_dist, total)
        return max_dist
        
    def run_tests(self):
        # Run all test cases with expected results
        print(f"--- Day {self.day:02d} Test Cases ---")
        for i, test_input in enumerate(self.test_inputs, 1):
            result = self.part1([test_input])
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
    solution = Day09()
    solution.run()
