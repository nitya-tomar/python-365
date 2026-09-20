# Count the occurrences of each letter in a word
def count_letters(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] = counts[letter] + 1
        else:
            counts[letter] = 1
    return counts

result = count_letters("hello")
print(result)