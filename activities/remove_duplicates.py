# Remove Duplicates Without Built-in Functions
# Remove duplicate elements from a list without using set(), dict.fromkeys(), or list comprehension tricks.

def remove_duplicates(lst):
    result = []
    for item in lst:
        found = False
        for existing in result:
            if existing == item:
                found = True
                break
        if not found:
            result.append(item)
    return result

# Test
lists = [
    [1, 2, 3, 2, 4, 1, 5],
    ["apple", "banana", "apple", "cherry", "banana"],
    [10, 10, 10, 10],
    [1, 2, 3, 4, 5],
]

for lst in lists:
    print(f"Original : {lst}")
    print(f"No Dupes : {remove_duplicates(lst)}")
    print()
