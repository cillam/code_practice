# Problem: Group Anagrams
# Difficulty: Medium
# Pattern:  (new one -- hash map / bucketing by a canonical key)
# Time:   |  Space:
#
# Given a list of strings `strs`, group the anagrams together. Return a list
# of groups (a list of lists). Anagrams are words made of the exact same
# letters in a different order ("eat" and "tea").
#
# The order of the groups, and the order of words within each group, does
# NOT matter -- the tests below normalize both sides before comparing, so
# don't worry about matching any particular ordering.
#
# The key question (that's a pun, you'll see): all anagrams of each other
# share something. What can you compute from a word that comes out IDENTICAL
# for every anagram of it, and DIFFERENT for non-anagrams? Whatever that is,
# it's your dictionary key.
#
# Brute force compares every pair of words: O(n^2 * k). The target groups in
# roughly O(n * k) (n words, k = word length) using a dict.
#
# Examples (shown in one possible order):
#   group(["eat","tea","tan","ate","nat","bat"])
#       -> [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#   group([""])    -> [[""]]
#   group(["a"])   -> [["a"]]
from collections import defaultdict

def group_anagrams(strs):
    anagram_dict = defaultdict(list)
    for s in strs:
        letters = tuple(sorted(s))
        anagram_dict[letters].append(s)
    return list(anagram_dict.values())


# --- test helper: normalizes group/word order so any valid grouping passes ---
def _norm(groups):
    return sorted(sorted(g) for g in groups)


if __name__ == "__main__":
    assert _norm(group_anagrams(["eat","tea","tan","ate","nat","bat"])) == \
        _norm([["bat"], ["nat","tan"], ["ate","eat","tea"]])
    assert _norm(group_anagrams([""])) == _norm([[""]])
    assert _norm(group_anagrams(["a"])) == _norm([["a"]])
    assert _norm(group_anagrams(["abc","bca","xyz","zyx","foo"])) == \
        _norm([["abc","bca"], ["xyz","zyx"], ["foo"]])
    print("passed")
