#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'euclideanDistance' and 'cosineSimilarity' functions below.
#
# Both functions are expected to return a DOUBLE.
# Both accept following parameters:
#  1. FLOAT_ARRAY u
#  2. FLOAT_ARRAY v
#

def euclideanDistance(u, v):
    distance = math.sqrt(sum((u_num - v_num)**2 for u_num, v_num in zip(u, v)))
    return distance


def cosineSimilarity(u, v):
    dot_product = sum(u_num * v_num for u_num, v_num in zip(u, v))
    length_of_u = math.sqrt(sum(u_num ** 2 for u_num in u))
    length_of_v = math.sqrt(sum(v_num ** 2 for v_num in v))
    if length_of_u == 0 or length_of_v == 0:
        similarity = 0.0
    else:
        similarity = dot_product / (length_of_u * length_of_v)
    return similarity

# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

TOL = 1e-6


def close(a, b):
    return a is not None and abs(a - b) <= TOL


# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = euclideanDistance([0, 0], [3, 4])
    assert close(result, 5.0), f"Sample 0 (euclidean): expected 5.0, got {result}"

    result = cosineSimilarity([1, 2, 3], [4, 5, 6])
    assert close(result, 0.9746318461970762), f"Sample 1 (cosine): expected 0.974632, got {result}"

    result = cosineSimilarity([1, 0], [0, 1])
    assert close(result, 0.0), f"Sample 2 (cosine): expected 0.0, got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(u, v, q):
    q.put((euclideanDistance(u, v), cosineSimilarity(u, v)))


def run_hidden_tests():
    passed = 0
    euclid_tests = [
        (([5], [5]), 0.0),
        (([1, 2, 3], [4, 6, 8]), math.sqrt(50)),
        (([-1, -1], [1, 1]), math.sqrt(8)),
        (([0.5, 1.5], [1.5, 0.5]), math.sqrt(2)),
    ]
    cosine_tests = [
        (([2, 4], [1, 2]), 1.0),           # same direction, different length
        (([1, 1], [-1, -1]), -1.0),        # opposite direction
        (([0, 0, 0], [1, 2, 3]), 0.0),     # zero vector: defined as 0.0
        (([3, 4], [4, 3]), 24 / 25),
    ]
    total = len(euclid_tests) + len(cosine_tests) + 1

    for i, ((u, v), expected) in enumerate(euclid_tests):
        if close(euclideanDistance(u, v), expected):
            passed += 1
        else:
            print(f"Hidden euclidean test {i} failed")

    for i, ((u, v), expected) in enumerate(cosine_tests):
        if close(cosineSimilarity(u, v), expected):
            passed += 1
        else:
            print(f"Hidden cosine test {i} failed")

    # Large input: vectors of length 100,000. Times out after 3 seconds.
    n = 100_000
    u = [1.0] * n
    v = [2.0] * n
    q = mp.Queue()
    p = mp.Process(target=_worker, args=(u, v, q))
    p.start()
    p.join(3)
    if p.is_alive():
        p.terminate()
        p.join()
        print("Large test failed (time limit exceeded)")
    else:
        e, c = q.get() if not q.empty() else (None, None)
        if close(e, math.sqrt(n)) and close(c, 1.0):
            passed += 1
        else:
            print("Large test failed (wrong answer)")

    print(f"Hidden tests: {passed}/{total} passed")


if __name__ == '__main__':
    run_sample_tests()
    run_hidden_tests()
