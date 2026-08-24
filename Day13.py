

#Step 1: create the empty dictionary and the loop, just print each number for now
#Here, every number appears only once — no duplicates. This list does not contain a duplicate.

#The task: write a function that checks a list and tells you True (yes, there's a duplicate) or False (no duplicates, everything's unique).

#Same pattern as before — walk through it with me first, small piece at a time.
def duplicate(numbers):
    seen = {}
    for num in numbers:
        if num in seen:
            return "duplicate found for " + str(num)+ " at index " + str(numbers.index(num))
        seen[num] = True
    return False

numbers = [1, 2, 3, 2, 5]


print(duplicate(numbers))