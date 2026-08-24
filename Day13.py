#The task: write a function that checks a list and tells you True (yes, there's a duplicate) or False (no duplicates, everything's unique).
def duplicate(numbers):
    seen = {}
    for index, num in enumerate(numbers):
        if num in seen:
            return "duplicate found for " + str(num) + " at index " + str(index)
        seen[num] = True
    return False

numbers = [1, 2, 3, 2, 5]
result = duplicate(numbers)
print(result)   