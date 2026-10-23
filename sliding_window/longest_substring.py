# Problem: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Pattern:  (new one -- sliding window)
# Time:   |  Space:
#
# Given a string `s`, return the LENGTH of the longest substring that
# contains no repeating characters.
#
# ("Substring" means contiguous -- a run of adjacent characters, not a
# subsequence. You're returning the length, an int, not the substring.)
#
# Brute force checks every substring for uniqueness: O(n^2) or worse. The
# target is O(n) with a sliding window -- a left and right edge defining a
# window that grows on the right and shrinks on the left as needed, so each
# character is visited a small constant number of times.
#
# Examples:
#   length_of_longest_substring("abcabcbb")  -> 3   # "abc"
#   length_of_longest_substring("bbbbb")     -> 1   # "b"
#   length_of_longest_substring("pwwkew")    -> 3   # "wke"  (not "pwke" -- not contiguous)
#   length_of_longest_substring("")          -> 0
#   length_of_longest_substring("dvdf")      -> 3   # "vdf"
#   length_of_longest_substring("abba")      -> 2   # watch this one carefully

def length_of_longest_substring(s):
    longest_len = 0
    current_dict = {}
    left = 0
    for right, char in enumerate(s):
        if char in current_dict:
            left = max(left, current_dict[char] + 1)
            current_dict[char] = right
        else:
            current_dict[char] = right
        if longest_len < right - left + 1:
            longest_len = right - left + 1
    return longest_len



if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("dvdf") == 3
    assert length_of_longest_substring("abba") == 2
    print("passed")
