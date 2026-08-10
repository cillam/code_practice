# Problem: Contains Duplicate
# Difficulty: Easy
# Pattern:
# Time:   |  Space:
#
# Given an integer list `nums`, return True if any value appears at least
# twice, and False if every element is distinct.
#
# Examples:
#   contains_duplicate([1, 2, 3, 1])        -> True
#   contains_duplicate([1, 2, 3, 4])        -> False
#   contains_duplicate([1, 1, 1, 3, 3, 4])  -> True

def contains_duplicate(nums):
    return len(nums) != len(set(nums))


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4]) is True
    print("passed")