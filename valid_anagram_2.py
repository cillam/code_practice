# anagrams.py
import time
from collections import defaultdict


# def groupAnagrams(words):
#     d = defaultdict(list)
#     for word in words:
#         letter_set = set(word)
#         letter_count = [word.count(char) for char in letter_set]
#         word_tuple = (*letter_set, *letter_count)
#         d[word_tuple].append(word)
#     return list(d.values())

def groupAnagrams(words):
    d = defaultdict(list)
    for word in words:
        d["".join(sorted(word))].append(word)
    return list(d.values())

# ---------------- SAMPLE TESTS (like "Run Code") ----------------
def run_sample_tests():
    result = groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
    assert result == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], f"Sample 0 got {result}"

    result = groupAnagrams(['abc', 'xyz', 'cab'])
    assert result == [['abc', 'cab'], ['xyz']], f"Sample 1 got {result}"

    print("Sample tests passed")


# ---------------- HIDDEN-STYLE TESTS (like "Submit") ----------------
# Try not to read these until you've written your solution.
def run_hidden_tests():
    passed = 0
    tests = [
        (['a'], [['a']]),
        (['x', 'y', 'z'], [['x'], ['y'], ['z']]),
        (['ab', 'ba', 'ab'], [['ab', 'ba', 'ab']]),
        (['aab', 'aba', 'abb', 'baa'], [['aab', 'aba', 'baa'], ['abb']]),
        (['listen', 'stone', 'silent', 'notes', 'enlist', 'onset'],
         [['listen', 'silent', 'enlist'], ['stone', 'notes', 'onset']]),
    ]
    for i, (words, expected) in enumerate(tests):
        result = groupAnagrams(words)
        if result == expected:
            passed += 1
        else:
            print(f"Hidden test {i} failed")

    # Large input: 100,000 words of length 100
    big = ['ab' * 50, 'ba' * 50] * 50_000
    start = time.time()
    result = groupAnagrams(big)
    elapsed = time.time() - start
    if len(result) == 1 and len(result[0]) == 100_000 and elapsed < 2:
        passed += 1
    else:
        print(f"Large test failed (took {elapsed:.2f}s)")

    print(f"Hidden tests: {passed}/{len(tests) + 1} passed")


if __name__ == '__main__':
    run_sample_tests()
    run_hidden_tests()