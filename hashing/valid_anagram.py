# Problem: Valid Anagram
# Difficulty: Easy
# Pattern: Character counting (set of both strings)
# Time: O(n * k), k = number of distinct characters  |  Space: O(n)


#def is_anagram(s, t):
#    return sorted(s) == sorted(t)

def is_anagram(s, t):
    letter_set = set(s + t)
    for char in letter_set:
        if s.count(char) != t.count(char):
            return False
    return True


print(is_anagram("anagram", "nagaram"))  #  True
print(is_anagram("rat", "car"))          #  False
print(is_anagram("a", "ab"))             #  False