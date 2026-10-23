# Coding Practice

My personal space for Python and ML/DS coding practice — LeetCode-style problems, algorithm drills, and small ML exercises. Private repo, low pressure, just reps.

## Structure

```
.
├── arrays/            # single-pass array scans (Kadane, running min/max)
├── hashing/           # hash maps / sets, counting, prefix sums
├── two_pointers/      # opposite-end or read/write pointers
├── sliding_window/    # same-direction pointers over a window
├── stack/             # LIFO problems
├── ml/                # numpy/pandas drills, from-scratch metrics & linear algebra
├── requirements.txt
└── README.md
```

Folders are by pattern rather than by difficulty — easier to find things when I'm reviewing a weak area. One file per problem, named in `snake_case` after the problem (e.g. `hashing/two_sum.py`, `sliding_window/longest_substring.py`). A `_2` / `_ii` suffix marks a revisit or variant of an earlier problem. New folders (e.g. `trees/`, `graphs/`, `dynamic_programming/`) get added as I reach those topics.

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

## Running a solution

Every file is self-checking — just run it directly:

```bash
python sliding_window/longest_substring.py
```

## Conventions

There are two file styles in the repo.

### 1. Header + inline asserts (LeetCode-style)

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

The header comment captures the pattern and complexity so future-me can skim and remember *why*, not just *what*. ML/DS drills add a `# Track: ML/DS coding` line at the top. Inline `assert`s act as quick self-checks and print `passed` when everything works.

### 2. HackerRank-style harness

These files start from a HackerRank-style stub (`# Complete the 'fnName' function below.`) with a camelCase function to fill in, followed by a built-in test harness:

- **Sample tests** (like "Run Code") — a few visible cases.
- **Hidden-style tests** (like "Submit") — edge cases plus a large input (~100,000 elements) run in a subprocess with a **3-second time limit**, so an O(n²) solution fails. Try not to read these before writing the solution.

Output ends with something like `Hidden tests: 7/7 passed`.

## Progress

| Date       | Problem                                         | File                                        | Topic                   | Difficulty |
|------------|-------------------------------------------------|---------------------------------------------|-------------------------|------------|
| 2026-08-07 | Two Sum                                         | `hashing/two_sum.py`                        | Hashing                 | Easy       |
| 2026-08-07 | Valid Anagram                                   | `hashing/valid_anagram.py`                  | Strings / counting      | Easy       |
| 2026-08-10 | Best Time to Buy and Sell Stock                 | `arrays/best_time_to_buy_sell_stock.py`     | Arrays                  | Easy       |
| 2026-08-10 | Contains Duplicate                              | `hashing/contains_dupe.py`                  | Hashing                 | Easy       |
| 2026-10-20 | Maximum Subarray                                | `arrays/maximum_subarray.py`                | Arrays                  | Easy+      |
| 2026-10-20 | Two Sum (revisit, timed harness)                | `hashing/two_sum_2.py`                      | Hashing                 | Easy       |
| 2026-10-20 | Group Anagrams (timed harness)                  | `hashing/group_anagrams_2.py`               | Hashing                 | Medium     |
| 2026-10-20 | Subarray Sum Equals K                           | `hashing/subarray_sum.py`                   | Prefix sum + hash map   | Medium     |
| 2026-10-21 | Valid Palindrome                                | `two_pointers/valid_palindrome.py`          | Two pointers            | Easy+      |
| 2026-10-21 | Move Zeroes                                     | `two_pointers/move_zeroes.py`               | Two pointers            | Easy+      |
| 2026-10-21 | Two Sum II – Input Array Is Sorted              | `two_pointers/two_sum_ii.py`                | Two pointers            | Medium     |
| 2026-10-21 | Container With Most Water                       | `two_pointers/container_with_most_water.py` | Two pointers            | Medium     |
| 2026-10-21 | Longest Substring Without Repeating Characters  | `sliding_window/longest_substring.py`       | Sliding window          | Medium     |
| 2026-10-21 | Contains Nearby Duplicate                       | `hashing/nearby_duplicates.py`              | Hashing                 | —          |
| 2026-10-21 | Pairs With Difference K                         | `hashing/pair_difference.py`                | Hashing                 | —          |
| 2026-10-21 | Pairs Divisible by K                            | `hashing/divisible_pairs.py`                | Hashing (remainders)    | —          |
| 2026-10-21 | Mean Squared Error                              | `ml/mean_squared_error.py`                  | ML/DS                   | Easy       |
| 2026-10-21 | Transpose & Matrix Multiply                     | `ml/matrix_ops.py`                          | ML/DS                   | —          |
| 2026-10-22 | Group Anagrams                                  | `hashing/group_anagrams.py`                 | Hashing (canonical key) | Medium     |
| 2026-10-22 | Count Target Pairs                              | `hashing/count_target_pairs.py`             | Hashing                 | —          |
| 2026-10-22 | Shortest Subarray With Sum ≥ Target             | `sliding_window/shortest_window.py`         | Sliding window          | —          |
| 2026-10-22 | Longest Substring With At Most K Distinct Chars | `sliding_window/k_distinct.py`              | Sliding window          | —          |
| 2026-10-22 | Evaluate Reverse Polish Notation                | `stack/eval_rpn.py`                         | Stack                   | Medium     |
| 2026-10-22 | Precision & Recall                              | `ml/precision_recall.py`                    | ML/DS                   | Easy       |
| 2026-10-22 | Euclidean Distance & Cosine Similarity          | `ml/vector_distance.py`                     | ML/DS                   | —          |

## Goals

- [ ] Build fluency with the core patterns (hashing, two pointers, sliding window, stack, BFS/DFS, DP)
- [ ] A few problems a week, consistency over volume
- [ ] Revisit anything that took more than one hint — spaced repetition beats cramming
- [ ] Fold in ML drills as the algorithm base gets solid
