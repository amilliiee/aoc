import sys
from pathlib import Path
from scipy.optimize import linprog

# Add utils to path  
sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.solution_template import Solution

class Day10(Solution):
    def __init__(self):
        super().__init__(day=10)
        
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
        tot_press = 0
        
        for line in data:
            target_str = line[line.index('[') + 1:line.index(']')]
            target = [1 if c == "#" else 0 for c in target_str]
            btn_options = line[line.index(']') + 1:line.index('{')].strip()
            
            buttons = []
            i = 0
            while i < len(btn_options):
                if btn_options[i] == '(':
                    j = btn_options.index(')', i)
                    btn_str = btn_options[i+1:j]
                    btn_lights = list(map(int, btn_str.split(','))) if btn_str else []
                    buttons.append(btn_lights)
                    i = j + 1
                else:
                    i += 1
            
            def solve_machine(tar, btns):
                n_lights = len(tar)
                n_btns = len(btns)
                min_press = float('inf')
                
                for mask in range(1 << n_btns): # 0 to 2^n_btns - 1
                    state = [0] * n_lights
                    
                    presses = 0
                    for i in range(n_btns):
                        if (mask >> i) & 1: # Btn i is pressed
                            presses += 1
                            for light in btns[i]:
                                state[light] ^= 1 # Toggle state
                    if state == target:
                        min_press = min(min_press, presses)
                return min_press
            
            min_press = solve_machine(target, buttons)
            tot_press += min_press
        return tot_press
    
    # def part2(self, data):
    #     def solve_joltage_bb(target, buttons):
    #         n_counters = len(target)
    #         n_buttons = len(buttons)

    #         # Calculate upper bounds and sort buttons (tight bounds first for better pruning)
    #         button_info = []
    #         for i, btn in enumerate(buttons):
    #             if btn:
    #                 max_p = min(target[c] for c in btn)
    #                 # Score: how "tight" the bound is (lower = better for pruning)
    #                 score = max_p
    #             else:
    #                 max_p = 0
    #                 score = 0
    #             button_info.append((score, max_p, i))

    #         # Sort by score ascending (tight bounds first)
    #         button_info.sort()
    #         sorted_indices = [i for _, _, i in button_info]
    #         sorted_buttons = [buttons[i] for i in sorted_indices]
    #         sorted_max_presses = [max_p for _, max_p, _ in button_info]

    #         best = float('inf')

    #         # Use iterative deepening DFS to find solution quickly
    #         def dfs(idx, current, presses_so_far):
    #             nonlocal best

    #             # Prune 1: already worse
    #             if presses_so_far >= best:
    #                 return False

    #             # Prune 2: optimistic lower bound
    #             remaining_needs = sum(max(0, target[i] - current[i]) for i in range(n_counters))
    #             if presses_so_far + remaining_needs >= best:
    #                 return False

    #             if idx == n_buttons:
    #                 if all(current[i] == target[i] for i in range(n_counters)):
    #                     best = presses_so_far
    #                     return True
    #                 return False

    #             btn = sorted_buttons[idx]
    #             max_k = sorted_max_presses[idx]

    #             # Try in increasing order (0 first often works)
    #             for k in range(max_k + 1):
    #                 # Quick update and check
    #                 new_current = current[:]
    #                 valid = True
    #                 for counter in btn:
    #                     new_current[counter] += k
    #                     if new_current[counter] > target[counter]:
    #                         valid = False
    #                         break
                        
    #                 if valid:
    #                     if dfs(idx + 1, new_current, presses_so_far + k):
    #                         return True  # Found optimal for this branch

    #             return False

    #         # Start with high bound and tighten
    #         dfs(0, [0]*n_counters, 0)
    #         return best
        
    #     total_presses = 0
    def part2(self, data):
        total_presses = 0

        for line in data:
            # Parse joltage
            joltage_str = line[line.index('{') + 1:line.index('}')]
            goal = list(map(int, joltage_str.split(',')))

            # Parse buttons
            btn_options = line[line.index(']') + 1:line.index('{')].strip()
            moves = []
            i = 0
            while i < len(btn_options):
                if btn_options[i] == '(':
                    j = btn_options.index(')', i)
                    btn_str = btn_options[i+1:j]
                    btn_lights = list(map(int, btn_str.split(','))) if btn_str else []
                    moves.append(set(btn_lights))
                    i = j + 1
                else:
                    i += 1

            # Set up integer linear programming
            n_counters = len(goal)
            n_buttons = len(moves)

            # Cost: minimize total presses
            c = [1] * n_buttons

            # Equality constraints: A_eq * x = goal
            A_eq = [[1 if i in moves[j] else 0 for j in range(n_buttons)] 
                    for i in range(n_counters)]

            # Bounds: x >= 0 (non-negative)
            bounds = [(0, None)] * n_buttons

            # Solve
            result = linprog(c, A_eq=A_eq, b_eq=goal, bounds=bounds, integrality=[1]*n_buttons, method='highs')

            if result.success:
                total_presses += int(result.fun)  # Total presses
            else:
                print(f"Failed to solve: {line}")

        return total_presses
    
        for line in data:
            # Parse line
            joltage_str = line[line.index('{') + 1:line.index('}')]
            target = list(map(int, joltage_str.split(',')))

            btn_options = line[line.index(']') + 1:line.index('{')].strip()
            buttons = []
            i = 0
            while i < len(btn_options):
                if btn_options[i] == '(':
                    j = btn_options.index(')', i)
                    btn_str = btn_options[i+1:j]
                    btn_lights = list(map(int, btn_str.split(','))) if btn_str else []
                    buttons.append(btn_lights)
                    i = j + 1
                else:
                    i += 1

            min_presses = solve_joltage_bb(target, buttons)
            total_presses += min_presses

        return total_presses
        
    def run(self):
        if not hasattr(self, 'test_inputs'):
            self.load_data()
        
        import argparse
        parser = argparse.ArgumentParser(description=f'Run Day 10 solutions')
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
            print(f"--- Day 10 Test Cases ---")
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
    solution = Day10()
    solution.run()
