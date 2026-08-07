# Coding Practice

My personal space for Python and ML/DS coding practice — LeetCode-style problems, algorithm drills, and small ML exercises. Private repo, low pressure, just reps.

## Structure

```
.
├── arrays/
├── strings/
├── hashing/
├── two-pointers/
├── trees/
├── graphs/
├── dynamic-programming/
├── ml/                # numpy/pandas drills, from-scratch implementations, etc.
└── README.md
```

Folders are by topic rather than by difficulty — easier to find things when I'm reviewing a weak area. One file per problem, named after the problem (e.g. `two-sum.py`, `valid-anagram.py`).

## Setup

```bash
# Create and activate a virtual environment
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Mac / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

In VS Code, `Ctrl/Cmd + Shift + P` → **Python: Select Interpreter** → pick the one in `.venv`.

## Conventions

Each solution file follows a simple template:

```python
# Problem: Two Sum
# Difficulty: Easy
# Pattern: Hash map / one-pass
# Time: O(n)  |  Space: O(n)

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("passed")
```

The header comment captures the pattern and complexity so future-me can skim and remember *why*, not just *what*. Inline `assert`s act as quick self-checks — run the file directly to confirm it works.

## Progress

| Date       | Problem        | Topic   | Difficulty | Notes                          |
|------------|----------------|---------|------------|--------------------------------|
| 2026-08-07 | Two Sum        | Hashing | Easy       | One-pass hash map              |
| 2026-08-07 | Valid Anagram  | Strings | Easy       | Set-of-both-strings + counts   |

## Goals

- [ ] Build fluency with the core patterns (hashing, two pointers, sliding window, BFS/DFS, DP)
- [ ] A few problems a week, consistency over volume
- [ ] Revisit anything that took more than one hint — spaced repetition beats cramming
- [ ] Fold in ML drills as the algorithm base gets solid
