# Problem: Move Zeroes
# Difficulty: Easy with a twist
# Pattern:
# Time:   |  Space:
#
# Given an integer array `nums`, move all 0's to the end of it while keeping
# the relative order of the non-zero elements.
#
# The twist: do it IN PLACE. You must modify `nums` itself rather than
# building and returning a new list. (The function returns None; the tests
# check nums after the call.) Aim to avoid making a full copy of the array.
#
# Examples:
#   [0, 1, 0, 3, 12]  ->  [1, 3, 12, 0, 0]
#   [0]               ->  [0]
#   [1, 2, 3]         ->  [1, 2, 3]
#   [0, 0, 1]         ->  [1, 0, 0]

def move_zeroes(nums):
    zero_index = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1



if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    assert a == [1, 3, 12, 0, 0], a

    b = [0]
    move_zeroes(b)
    assert b == [0], b

    c = [1, 2, 3]
    move_zeroes(c)
    assert c == [1, 2, 3], c

    d = [0, 0, 1]
    move_zeroes(d)
    assert d == [1, 0, 0], d

    print("passed")
