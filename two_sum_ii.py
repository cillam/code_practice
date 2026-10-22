# Problem: Two Sum II - Input Array Is Sorted
# Difficulty: Medium  (Python graduation test -- UNAIDED)
# Approach:
# Time: O(n)  |  Space: O(1)
#
# Given a 1-INDEXED array of integers `numbers` that is already sorted in
# non-decreasing order, find two numbers that add up to `target`.
#
# Return the two indices (1-indexed) as a list [index1, index2], where
# index1 < index2. There is exactly one solution, and you may not use the
# same element twice.
#
# Aim for O(n) time and O(1) space. The fact that the array is SORTED is the
# thing that makes that possible -- that's the part to think about.
#
# Examples:
#   two_sum([2, 7, 11, 15], 9)              -> [1, 2]   # 2 + 7 = 9
#   two_sum([2, 3, 4], 6)                   -> [1, 3]   # 2 + 4 = 6
#   two_sum([-1, 0], -1)                    -> [1, 2]   # -1 + 0 = -1
#   two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8)  -> [4, 5]   # 4 + 4 = 8

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if target == current_sum:
            return [left + 1, right + 1]
        elif target < current_sum:
            right -= 1
        else:
            left += 1


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
    assert two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8) == [4, 5]
    print("passed")
