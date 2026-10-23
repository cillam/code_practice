#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target


# O(n) time, O(1) space

def shortestSubarray(nums, target):
    # Sliding window with two pointers moving in same directions
    # all values are positive, so shrinking always lowers the sum and the pointers never back up
    left = 0
    shortest = len(nums) + 1
    current_total = 0
    for right, num in enumerate(nums):
        current_total += num
        # check if current window sum is equal to or greater than target
        while current_total >= target:
            shortest = min(shortest, right - left + 1)
            current_total -= nums[left]
            left += 1
    if shortest == len(nums) + 1: # longer than any real window = "none found"
        return 0
    return shortest


# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = shortestSubarray([2, 3, 1, 2, 4, 3], 7)
    assert result == 2, f"Sample 0: expected 2, got {result}"

    result = shortestSubarray([1, 1, 1, 1], 10)
    assert result == 0, f"Sample 1: expected 0, got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(nums, target, q):
    q.put(shortestSubarray(nums, target))


def run_hidden_tests():
    passed = 0
    tests = [
        (([7], 7), 1),
        (([5], 7), 0),
        (([1, 4, 4], 4), 1),
        (([1, 2, 3, 4, 5], 15), 5),
        (([1, 2, 3, 4, 5], 11), 3),
        (([10, 1, 1, 1, 10], 11), 2),
        (([1, 1, 1, 1, 1, 1, 1, 1], 11), 0),
    ]
    for i, ((nums, target), expected) in enumerate(tests):
        result = shortestSubarray(nums, target)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: n = 100,000. Times out after 3 seconds.
    big, target, expected = [1] * 99_999 + [100_000], 100_000, 1
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
