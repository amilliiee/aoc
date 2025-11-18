# Advent of Code 2015
Python solutions for [Advent of Code 2015](https://adventofcode.com/2015)

## Progress
**16/50 Stars** ⭐ 🔄 In Progresss

| Day | Challenge | Pt.1 | Pt.2 | Notes |
| --- | --------- | ---- | ---- | ----- |
| 1 | Not Quite Lisp |⭐|⭐| Counting floors |
| 2 | I Was Told There Would Be No Math |⭐|⭐| Total amount of wrapping paper and ribbon |
| 3 | Perfectly Spherical Houses in a Vacuum |⭐|⭐| Present delivery without and with a second Santa |
| 4 | The Ideal Stocking Stuffer |⭐|⭐| MD5 hashes and hexadecimal |
| 5 | Doesn't He Have Intern-Elves For This? |⭐|⭐| String parsing for 'naughty' or 'nice' |
| 6 | Probably a Fire Hazard |⭐|⭐| Toggling lights in a 1000x1000 grid |
| 7 | Some Assembly Required |⭐|⭐| Recursion, so much recursion |
| 8 | Matchsticks |⭐|⭐| String literals vs. characters in memory |
| 9 | All in a Single Night |⭐|⭐| The traveling salesman problem for Santa |
| 10 | Elves Look, Elves Say |  |  |  |
| 11 | Corporate Policy |  |  |  |
| 12 | JSAbacusFramework.io |  |  |  |
| 13 | Knights of the Dinner Table |  |  |  |
| 14 | Reindeer Olympics |  |  |  |
| 15 | Science for Hungry People |  |  |  |
| 16 | Aunt Sue |  |  |  |
| 17 | No Such Thing as Too Much |  |  |  |
| 18 | Like a GIF For Your Yard |  |  |  |
| 19 | Medicine for Rudolph |  |  |  |
| 20 | Infinite Elves and Infinite Houses |  |  |  |
| 21 | RPG Simulator 20xx |  |  |  |
| 22 | Wizard Simulator 20xx |  |  |  |
| 23 | Opening the Turing Lock |  |  |  |
| 24 | It Hangs in the Balance |  |  |  |
| 25 | Let It Snow |  |  |  |

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
- test.txt: Test cases with expected results
```text
# Test case -> Solution
Test case
```
- utils/: Shared utilities and templates

## Learning Points
- Constraint optimization
- Combinatorial mathematics
- Performance tuning for large search spaces