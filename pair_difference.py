#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'countPairsWithDifference' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

def countPairsWithDifference(nums, k):
    # Create dictionary to count values seen before
    # Look up partners before recording new value to dict
    # Check for two partners: num - k, num + k
    # O(n) time, O(n) space
    seen = defaultdict(int)
    count = 0
    for num in nums:
        partner1 = num - k
        if partner1 in seen:
            count += seen[partner1]
        if k != 0:
            partner2 = num + k
            if partner2 in seen:
                count += seen[partner2]
        seen[num] = seen[num] + 1
    return count


# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = countPairsWithDifference([1, 5, 3, 4, 2], 2)
    assert result == 3, f"Sample 0: expected 3, got {result}"

    result = countPairsWithDifference([1, 2, 2, 1], 1)
    assert result == 4, f"Sample 1: expected 4, got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(nums, k, q):
    q.put(countPairsWithDifference(nums, k))


def run_hidden_tests():
    passed = 0
    tests = [
        (([7], 3), 0),
        (([1, 1, 1], 0), 3),
        (([4, 4, 8], 0), 1),
        (([3, 1, 4, 1, 5], 2), 3),
        (([-2, 0, 2, -4], 2), 3),
        (([10, 20, 30], 5), 0),
    ]
    for i, ((nums, k), expected) in enumerate(tests):
        result = countPairsWithDifference(nums, k)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: n = 100,000. Times out after 3 seconds.
    big, k, expected = [1] * 100_000, 0, 4_999_950_000
    q = mp.Queue()
    p = mp.Process(target=_worker, args=(big, k, q))
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
