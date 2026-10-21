#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'twoSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def twoSum(nums, target):
    seen = dict()
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[num] = i

# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = twoSum([2, 7, 11, 15], 9)
    assert result == [0, 1], f"Sample 0: expected [0, 1], got {result}"

    result = twoSum([3, 2, 4], 6)
    assert result == [1, 2], f"Sample 1: expected [1, 2], got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(nums, target, q):
    q.put(twoSum(nums, target))


def run_hidden_tests():
    passed = 0
    tests = [
        (([3, 3], 6), [0, 1]),
        (([-3, 4, 3, 90], 0), [0, 2]),
        (([0, 4, 3, 0], 0), [0, 3]),
        (([1, 5, 9, -2], 7), [2, 3]),
        (([5, 1, 5], 10), [0, 2]),
    ]
    for i, ((nums, target), expected) in enumerate(tests):
        result = twoSum(nums, target)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: n = 100,000. Times out after 3 seconds.
    big, target, expected = list(range(100_000)), 199_997, [99_998, 99_999]
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
