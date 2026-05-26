# Palindrome Checker
# A string is a palindrome if it reads the same forward and backward.
# Example: "racecar", "madam", "level"

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

# Test
words = ["racecar", "hello", "madam", "level", "Python", "A man a plan a canal Panama"]
for word in words:
    result = "Palindrome" if is_palindrome(word) else "Not a Palindrome"
    print(f'"{word}" => {result}')
