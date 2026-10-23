#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'countTargetPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def countTargetPairs(nums, target):
    seen = defaultdict(int)
    count = 0
    for num in nums:
        complement = target - num
        count += seen[complement]
        seen[num] += 1
    return count

# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = countTargetPairs([1, 5, 7, -1], 6)
    assert result == 2, f"Sample 0: expected 2, got {result}"

    result = countTargetPairs([1, 1, 1, 1], 2)
    assert result == 6, f"Sample 1: expected 6, got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(nums, target, q):
    q.put(countTargetPairs(nums, target))


def run_hidden_tests():
    passed = 0
    tests = [
        (([4], 8), 0),
        (([4, 4], 8), 1),
        (([3, 3, 3], 6), 3),
        (([-2, 2, 0, 0], 0), 2),
        (([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11), 9),
        (([1, 2, 3], 100), 0),
    ]
    for i, ((nums, target), expected) in enumerate(tests):
        result = countTargetPairs(nums, target)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: n = 100,000. Times out after 3 seconds.
    big, target, expected = [5] * 100_000, 10, 4_999_950_000
    q = mp.Queue()
    p = mp.Process(target=_worker, args=(big, target, q))
    p.start()
    p.join(3)
    if p.is_alive():
        p.terminate()
        p.join()
        print("Large test failed (time limit exceeded)")
    elif not q.empty() and q.get() == expected:
        passed += 1
    else:
        print("Large test failed (wrong answer)")

    print(f"Hidden tests: {passed}/{len(tests) + 1} passed")


if __name__ == '__main__':
    run_sample_tests()
    run_hidden_tests()
