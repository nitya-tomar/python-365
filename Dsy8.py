#Given numbers = [10, 20, 30, 40, 50, 60], print only the last 3 items using slicing.

numbers = [10, 20, 30, 40, 50, 60]
# Using slicing to get the last 3 items
newlist = numbers[-3:]
print(newlist)  


#Given cpu_usage = [45, 92, 78, 60, 88], use a loop to count how many values are above 80.
cpu_usage = [45, 92, 78, 60, 88]
count=0
for usage in cpu_usage: 
    if usage > 80:
        count += 1
print(count)               