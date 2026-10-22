# Problem: Maximum Subarray
# Difficulty: Easy with a twist
# Pattern:
# Time:   |  Space:
#
# Given an integer array `nums`, find the contiguous subarray (containing at
# least one number) with the largest sum, and return that sum.
#
# Examples:
#   max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6   # subarray [4, -1, 2, 1]
#   max_subarray([1])                              -> 1
#   max_subarray([5, 4, -1, 7, 8])                 -> 23
#   max_subarray([-3, -1, -2])                     -> -1  # all negative: pick the least-bad

def max_subarray(nums):
    current = 0
    best = min(nums)
    for i in range(len(nums)):
        current = max(nums[i], current + nums[i])
        best = max(best, current)
    return best


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-3, -1, -2]) == -1
    print("passed")
