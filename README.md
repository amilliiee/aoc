# Advent of Code Solutions
My solutions to [Advent of Code](https://adventofcode.com/) challenges, starting at the beginning.

## Years Completed
|Year|Language|Stars|Status|
|----|--------|-----|------|
[2015](./2015/)|Python|24/50|⏸️ Paused|
[2016](./2016/)|  |0/50|❌ Not Started|
[2017](./2017/)|  |0/50|❌ Not Started|
[2018](./2018/)|  |0/50|❌ Not Started|
[2019](./2019/)|  |0/50|❌ Not Started|
[2020](./2020/)|  |0/50|❌ Not Started|
[2021](./2021/)|  |0/50|❌ Not Started|
[2022](./2022/)|  |0/50|❌ Not Started|
[2023](./2023/)|  |0/50|❌ Not Started|
[2024](./2024/)|  |0/50|❌ Not Started|
[2025](./2025/)|Python|6/24|🔄 In Progress|

## Project Structure
Each year follows this organization:
```text
year/
├── README
├── day01/
│ ├── solution.py
│ ├── input.txt
│ └── test.txt
├── day02/
└── ...
Days I find particularly challenging will also include a README.
```

## Setup and Running:
```bash
# Create a new day (from root of project)
python create_day.py <year> <day> # python create_day.py 2025 10 creates day 10 of 2025

# Run a specific day
cd 2015/day03 && python solution.py

# Run with options
cd 2015/day03 && python --part 1 --test

# Available options when running solutions:
python solution.py --part 1        # Run only part 1
python solution.py --test          # Run only tests
python solution.py --real          # Run only real data (the provided input)
python solution.py --part 2 --test # Run only part 2 tests
```

**2015 days 1-12 used the old format below**
```bash
# Create a new day
python create_day.py 2 # Create day 2

# Run a specific day
cd 2015/day02 && python solution.py

# Run multiple or all days
python run_all.py 1 2 5 # Run days 1, 2, and 5
python run_all.py       # Run all available days
```

## Progress Tracking
- ✅ Completed
- 🔄 In Progress
- ⏸️ Paused
- ❌ Not Started

## Goals of this pursuit:
- Complete all available years
- Implement in multiple languages
- Optimize solutions for performance
- Add detailed explanations