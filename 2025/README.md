# Advent of Code 2015
Python solutions for [Advent of Code 2015](https://adventofcode.com/2015)

## Progress
**22/24 Stars** ⭐ 🔄 In Progresss

|Day|Challenge|Pt.1|Pt.2|Notes|
|---|---------|----|----|-----|
|1|Secret Entrance|⭐|⭐|Counting zeroes two ways|
|2|Gift Shop|⭐|⭐|Repeating patterns in numbers|
|3|Lobby|⭐|⭐|Finding maximum combinations of numbers|
|4|Printing Department|⭐|⭐|Counting and removing paper rolls|
|5|Cafeteria|⭐|⭐|Intersections and unions of ingredients|
|6|Trash Compactor|⭐|⭐|Cephalopod math|
|7|Laboratories|⭐|⭐|Tracing a splitting beam|
|8|Playground|⭐|⭐|Too many lights|
|9|Movie Theater|⭐|⭐|Rectangles everywhere|
|10|Factory|⭐|⭐|XOR and AND for lights and joltage|
|11|Reactor|⭐|⭐|DFS for pathing with and without requirements|
|12|Christmas Tree Farm|⭐|⭐|Present packing|


## Running Solutions
```bash
# Run specific day
cd day01
python solution.py

# Run with test data only
python solution.py --test

# Run multiple or all days
python run_all.py 1 2 5 # Run days 1, 2, and 5
python run_all.py       # Run all available days
```

## Structure
- solution.py: Main solution file
- input.txt: Puzzle input
- test.txt: Test cases (aka the values used as an example)
```
- utils/: Shared utilities and templates

## Learning Points
- Constraint optimization
- Combinatorial mathematics
- Performance tuning for large search spaces