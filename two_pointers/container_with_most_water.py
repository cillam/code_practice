# Problem: Container With Most Water
# Difficulty: Medium  (Python graduation test)
# Approach:
# Time:   |  Space:
#
# You are given an integer array `height` of length n. There are n vertical
# lines; line i goes from (i, 0) up to (i, height[i]).
#
# Pick two lines that, together with the x-axis, form a container holding the
# most water. Return that maximum amount of water (an area).
#
# The water a pair (i, j) holds is limited by the SHORTER of the two lines:
#
#     area = min(height[i], height[j]) * (j - i)
#
# (The container can't hold water above its shorter wall, and width is the
# distance between the two lines.) You may not slant the container.
#
# The brute-force answer checks every pair: O(n^2). A clean solution runs in
# O(n) time and O(1) space. Aim for that one -- this is the graduation test.
#
# Examples:
#   max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])  -> 49   # lines at idx 1 and 8: min(8,7)*7
#   max_area([1, 1])                        -> 1
#   max_area([4, 3, 2, 1, 4])               -> 16   # the two 4's at the ends: 4*4
#   max_area([1, 2, 1])                     -> 2

def max_area(height):
    best_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        if area > best_area:
            best_area = area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best_area


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("passed")
