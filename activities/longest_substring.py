# Longest Substring Without Repeating Characters
# Find the length and the actual substring that has no repeating characters.
# Example: "abcabcbb" => "abc" (length 3)

def longest_unique_substring(s):
    char_index = {}
    longest = ""
    start = 0

    for end in range(len(s)):
        char = s[end]

        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = end

        if end - start + 1 > len(longest):
            longest = s[start:end + 1]

    return longest

# Test
strings = ["abcabcbb", "bbbbb", "pwwkew", "dvdf", ""]
for s in strings:
    result = longest_unique_substring(s)
    print(f'"{s}" => Longest substring: "{result}", Length: {len(result)}')
