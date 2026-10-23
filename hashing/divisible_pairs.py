#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'countDivisiblePairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

def countDivisiblePairs(nums, k):
    # Pair numbers by remainder: r pairs with (k - r) % k.
    # Count remainders seen so far; one pass, O(n) time, O(k) space at most.
    seen = defaultdict(int)
    count = 0
    for num in nums:
        remainder = num % k
        complement_remainder = (k - remainder) % k
        if complement_remainder in seen:
            count += seen[complement_remainder]
        seen[remainder] += 1
    return count

countDivisiblePairs([1, 2, 3, 4, 5], 3)
# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = countDivisiblePairs([1, 2, 3, 4, 5], 3)
    assert result == 4, f"Sample 0: expected 4, got {result}"

    result = countDivisiblePairs([2, 2, 1, 7, 5, 3], 4)
    assert result == 5, f"Sample 1: expected 5, got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(nums, k, q):
    q.put(countDivisiblePairs(nums, k))


def run_hidden_tests():
    passed = 0
    tests = [
        (([5], 5), 0),
        (([3, 6, 9], 3), 3),
        (([1, 2, 3], 1), 3),
        (([0, 0, 0, 0], 7), 6),
        (([-1, 1, 4, -4], 5), 4),
        (([2, 4, 6, 8], 4), 2),
        (([1, 3, 5, 7, 9, 11], 6), 5),
    ]
    for i, ((nums, k), expected) in enumerate(tests):
        result = countDivisiblePairs(nums, k)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: n = 100,000. Times out after 3 seconds.
    big, k, expected = [1] * 100_000, 2, 4_999_950_000
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
