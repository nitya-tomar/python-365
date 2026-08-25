# Starting guest list
guests = ["Alice", "Bob", "Charlie", "David"]

# 1. Add "Eve" to the end of the guest list using a list method
guests.append("Eve")


# 2. Remove "Bob" from the list because he cannot attend
guests.remove("Bob")


# 3. Use a list method to print the final position/index of "Charlie"
charlie_index = guests.index("Charlie")
print(f"Charlie is at index: {charlie_index}") 
# Output: Charlie is at index: 1 (since Bob was removed)


# 4. Use range() to create a list of VIP table numbers from 1 to 5 (inclusive)
# We use 6 as the stop number because range() excludes the last number.
table_numbers = list(range(1, 6))
print(f"Table Numbers: {table_numbers}") 
# Output: Table Numbers: [1, 2, 3, 4, 5]


# 5. Use enumerate() and a for-loop to print each guest with their entry token number.
print("\n--- Guest Tokens ---")
for index, guest in enumerate(guests):
    print(f"Token #{index}: {guest}")
