#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hasNearbyDuplicate' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

def hasNearbyDuplicate(nums, k):
    # store values seen before
    seen = {}
    # loop through array
    for i, num in enumerate(nums):
        # check if in seen and distance between indexes
        if num in seen and k >= i - seen[num]:
            return "YES"
        # update seen with current num-index pair
        else:
            seen[num] = i
    return "NO"
    


# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = hasNearbyDuplicate([1, 2, 3, 1], 3)
    assert result == "YES", f"Sample 0: expected 'YES', got {result!r}"

    result = hasNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    assert result == "NO", f"Sample 1: expected 'NO', got {result!r}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(nums, k, q):
    q.put(hasNearbyDuplicate(nums, k))


def run_hidden_tests():
    passed = 0
    tests = [
        (([1, 0, 1, 1], 1), "YES"),
        (([5], 0), "NO"),
        (([1, 1], 0), "NO"),
        (([4, 4], 1), "YES"),
        (([1, 2, 1, 2, 1], 1), "NO"),
        (([7, 1, 7, 1, 7], 2), "YES"),
        (([-1, -1], 1), "YES"),
    ]
    for i, ((nums, k), expected) in enumerate(tests):
        result = hasNearbyDuplicate(nums, k)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: n = 100,000, all distinct. Times out after 3 seconds.
    big, k, expected = list(range(100_000)), 100_000, "NO"
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
