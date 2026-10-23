#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'longestKDistinct' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def longestKDistinct(s, k):
    # Sliding window with two pointer moving in the same direction with left
    # pointer closing when new character over k is introduced
    # Return length of longest substring as an integer
    longest_substring = 0
    left = 0
    current_dict = defaultdict(int)
    for right, char in enumerate(s):
        current_dict[char] += 1
        while len(current_dict) > k:
            current_dict[s[left]] -= 1
            if current_dict[s[left]] == 0:
                del current_dict[s[left]]
            left += 1
        if longest_substring < right - left + 1:
            longest_substring = right - left + 1
    return longest_substring



# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = longestKDistinct("eceba", 2)
    assert result == 3, f"Sample 0: expected 3, got {result}"

    result = longestKDistinct("aaabbcc", 1)
    assert result == 3, f"Sample 1: expected 3, got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(s, k, q):
    q.put(longestKDistinct(s, k))


def run_hidden_tests():
    passed = 0
    tests = [
        (("a", 1), 1),
        (("a", 0), 0),
        (("abc", 5), 3),
        (("aabbcc", 2), 4),
        (("abaccc", 2), 4),
        (("abcabcabc", 2), 2),
        (("abcadcacacaca", 3), 11),
    ]
    for i, ((s, k), expected) in enumerate(tests):
        result = longestKDistinct(s, k)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: n = 100,000. Times out after 3 seconds.
    big = "ab" * 25_000 + "c" * 50_000
    k, expected = 2, 50_001
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
