from collections import Counter
# Read input and split into a list of integers
numbers = list(map(int, input().split()))

# Extract n and the list of values
n = numbers[0]
values = numbers[1:]

# Count frequency of each number
frequency = Counter(values)

# Find the mode (most frequent element)
mode = max(frequency, key=frequency.get)

# Print the mode
print(mode)
