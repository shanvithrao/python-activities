# Anagram Checker
# Two strings are anagrams if they contain the same characters in the same frequency.
# Example: "listen" and "silent" are anagrams.

def are_anagrams(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    if len(str1) != len(str2):
        return False

    count = {}

    for ch in str1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in str2:
        if ch in count:
            count[ch] -= 1
        else:
            return False

    for val in count.values():
        if val != 0:
            return False

    return True

# Test
pairs = [("listen", "silent"), ("hello", "world"), ("Triangle", "Integral"), ("abc", "cab")]
for a, b in pairs:
    result = "Anagram" if are_anagrams(a, b) else "Not an Anagram"
    print(f{a}
