#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'transpose' and 'matrixMultiply' functions below.
#
# transpose is expected to return a 2D_INTEGER_ARRAY.
# It accepts 2D_INTEGER_ARRAY matrix as parameter.
#
# matrixMultiply is expected to return a 2D_INTEGER_ARRAY.
# It accepts following parameters:
#  1. 2D_INTEGER_ARRAY a
#  2. 2D_INTEGER_ARRAY b
#

def transpose(matrix):
    transposed = [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

    return transposed

def transpose(matrix):
    # Row i of the result is column i of the input. O(r * c).
    return [list(col) for col in zip(*matrix)]

def matrixMultiply(a, b):
    multiplied_matrix = []
    if len(a[0]) != len(b):
        return []
    b_transpose = transpose(b)
    for i in range(len(a)):
        new_row = []
        for j in range(len(b_transpose)):
            total = 0
            for k in range(len(a[0])):
                product = a[i][k] * b_transpose[j][k]
                total += product
            new_row.append(total)
        multiplied_matrix.append(new_row)
    return multiplied_matrix

# ============================================================================
# Everything below is the practice harness, not part of your solution.
# ============================================================================

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = transpose([[1, 2, 3], [4, 5, 6]])
    assert result == [[1, 4], [2, 5], [3, 6]], f"Sample 0 (transpose): got {result}"

    result = matrixMultiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    assert result == [[19, 22], [43, 50]], f"Sample 1 (multiply): got {result}"

    result = matrixMultiply([[1, 2, 3]], [[4], [5], [6]])
    assert result == [[32]], f"Sample 2 (multiply): got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
import multiprocessing as mp


def _worker(a, b, q):
    q.put(matrixMultiply(a, b))


def run_hidden_tests():
    passed = 0
    transpose_tests = [
        ([[7]], [[7]]),
        ([[1, 2, 3]], [[1], [2], [3]]),
        ([[1], [2], [3]], [[1, 2, 3]]),
        ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
    ]
    multiply_tests = [
        (([[3]], [[-2]]), [[-6]]),
        (([[1, 2], [3, 4]], [[1, 0], [0, 1]]), [[1, 2], [3, 4]]),
        (([[4], [5], [6]], [[1, 2, 3]]), [[4, 8, 12], [5, 10, 15], [6, 12, 18]]),
        (([[1, -1, 2], [0, 3, 1]], [[2, 1], [1, 0], [0, -2]]), [[1, -3], [3, -2]]),
        (([[1, 2], [3, 4]], [[1, 2, 3]]), []),   # incompatible shapes
        (([[0, 0], [0, 0]], [[5, 6], [7, 8]]), [[0, 0], [0, 0]]),
    ]
    total = len(transpose_tests) + len(multiply_tests) + 1

    for i, (m, expected) in enumerate(transpose_tests):
        result = transpose(m)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden transpose test {i} failed")

    for i, ((a, b), expected) in enumerate(multiply_tests):
        result = matrixMultiply(a, b)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden multiply test {i} failed")

    # Large input: 100 x 100 matrix times the identity. Times out after 3 seconds.
    n = 100
    big = [[r * n + c for c in range(n)] for r in range(n)]
    identity = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
    q = mp.Queue()
    p = mp.Process(target=_worker, args=(big, identity, q))
    p.start()
    p.join(3)
    if p.is_alive():
        p.terminate()
        p.join()
        print("Large test failed (time limit exceeded)")
    elif not q.empty() and q.get() == big:
        passed += 1
    else:
        print("Large test failed (wrong answer)")

    print(f"Hidden tests: {passed}/{total} passed")


if __name__ == '__main__':
    run_sample_tests()
    run_hidden_tests()
