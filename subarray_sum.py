#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'countSubarrays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

def countSubarrays(nums, k):
    seen = defaultdict(int)
    current_total = 0
    seen[current_total] = 1
    num_of_arrays = 0
    for n in nums:
        current_total += n
        num_of_arrays += seen[current_total-k]
        seen[current_total] = seen[current_total] + 1
    return num_of_arrays



# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = countSubarrays([1, 1, 1], 2)
    assert result == 2, f"Sample 0: expected 2, got {result}"

    result = countSubarrays([1, 2, 3], 3)
    assert result == 2, f"Sample 1: expected 2, got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(nums, k, q):
    q.put(countSubarrays(nums, k))


def run_hidden_tests():
    passed = 0
    tests = [
        (([5], 5), 1),
        (([5], 1), 0),
        (([0, 0, 0], 0), 6),
        (([1, -1, 0], 0), 3),
        (([-1, -1, 1], 0), 1),
        (([3, 4, 7, 2, -3, 1, 4, 2], 7), 4),
    ]
    for i, ((nums, k), expected) in enumerate(tests):
        result = countSubarrays(nums, k)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: n = 100,000. Times out after 3 seconds.
    big, k, expected = [1] * 100_000, 50_000, 50_001
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