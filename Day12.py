def two_sum_fast(numbers, target):
    seen = {}
    for index, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index

result = two_sum_fast([2, 7, 11, 15], 18)
print(result)