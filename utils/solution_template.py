from utils.file_reader import read_input, read_lines

class Solution:
  def __init__(self, day):
    self.day = day
    self.test_data = None
    self.real_data = None
    
  def load_data(self):
    # Load both test and real data
    self.test_data = read_input(self.day, test=True)
    self.real_data = read_input(self.day, test=False)
    return self
  
  def part1(self, data):
    # Override this method
    raise NotImplementedError('part1 not implemented')
  
  def part2(self, data):
    # Override this method
    raise NotImplementedError('part2 not implemented')
  
  def run(self):
    # Run both parts with test and real data
    if not self.test_data or not self.real_data:
      self.load_data()
      
    print(f"--- Day {self.day:02d} ---")
    
    # Test part 1
    try:
      test_result1 = self.part1(self.test_data)
      print(f"Part 1 Test: {test_result1}")
    except Exception as e:
      print(f"Part 1 Test Failed: {e}")
    
    # Real part 1
    try:
      real_result1 = self.part1(self.real_data)
      print(f"Part 1 Real: {real_result1}")
    except Exception as e:
      print("Part 1 Real Failed: {e}")
    
    # Test part 2
    try:
      test_result2 = self.part1(self.test_data)
      print(f"Part 2 Test: {test_result2}")
    except Exception as e:
      print(f"Part 2 Test Failed: {e}")
    
    # Real part 2
    try:
      real_result2 = self.part1(self.real_data)
      print(f"Part 2 Real: {real_result2}")
    except Exception as e:
      print("Part 2 Real Failed: {e}")
      
    print()