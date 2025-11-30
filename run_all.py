from pathlib import Path
import importlib
import sys

def run_day(day):
  # Run solution for specific day
  try:
    day_str = f"day{day:02d}"
    module = importlib.import_module(f"{day_str}.solution")
    solution_class = getattr(module, f"Day{day:02d}")
    solution = solution_class()
    solution.run()
  except Exception as e:
    print(f"Error running dat {day}: {e}")
    
def run_all():
    # Run all available days
    for day in range(1, 26):
        day_dir = Path(f"day{day:02d}")
        if day_dir.exists():
            run_day(day)

def run_specific(days):
    # Run specific days
    for day in days:
        run_day(day)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run specific days: python run_all.py 1 2 5
        days = [int(arg) for arg in sys.argv[1:]]
        run_specific(days)
    else:
        # Run all days
        run_all()