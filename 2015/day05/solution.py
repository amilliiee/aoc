import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent.parent))

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
            return [line.strip() for line in f]
    
    def part1(self, data):
        # Find 'nice' string based on rules
        # At least three vowels, at least one double letter, and doesn't contain 'ab', 'cd', 'pq', 'xy'
        nice = 0
        vowels = 'aeiou'
        forbidden = ['ab', 'cd', 'pq', 'xy']
        
        for line in data:
            double = False
            if any(chars in line for chars in forbidden):
                continue
            
            vowel_count = sum(1 for char in line if char in vowels)
            
            for i in range(len(line) - 1):
                if line[i] == line[i + 1]:
                    double = True
                    break
            
            if (vowel_count >= 3 and double):
                nice += 1
            
        return nice
        
    
    def part2(self, data):
        # Similar to part 1 but the rules have changed
        # Contains a pair of any two letters that appears at least twice in the string without overlapping (aa vs aaa) and contains at least one letter which repeats with exactly one letter between them (xyx, efe, even aaa)
        nice = 0
        
        for line in data:
            rule1 = False
            rule2 = False
            pairs = {}
            
            for i in range(len(line) - 1):
                pair = line[i:i+2]
                
                if pair in pairs:
                    if i >= pairs[pair] + 2:
                        rule1 = True
                        break
                else:
                    pairs[pair] = i
            
            for i in range(len(line) - 2):
                if line[i] == line[i+2]:
                    rule2 = True
                    break
            
            if rule1 and rule2:
                nice += 1
        return nice
        
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
    solution = Day05()
    solution.run()
