# Problem: Valid Palindrome
# Difficulty: Easy with a twist
# Pattern:
# Time:   |  Space:
#
# A phrase is a palindrome if, after converting all uppercase letters to
# lowercase and removing all non-alphanumeric characters, it reads the same
# forward and backward. Given a string `s`, return True if it is a palindrome,
# otherwise False.
#
# The twist: you have to handle the cleaning (case + punctuation + spaces)
# AND the comparison. Try to do the comparison with two pointers moving
# inward from both ends, rather than building a reversed copy of the string.
#
# Examples:
#   is_palindrome("A man, a plan, a canal: Panama")  -> True
#   is_palindrome("race a car")                      -> False
#   is_palindrome(" ")                               -> True   # empty after cleaning
#   is_palindrome("0P")                              -> False  # '0' vs 'p', digits count
#   is_palindrome("Able was I, ere I saw Elba")      -> True

def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("Able was I, ere I saw Elba") is True
    print("passed")