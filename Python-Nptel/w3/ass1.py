numbers = list(map(int, input().split()))
unique_numbers = list(set(numbers))  # Remove duplicates
unique_numbers.sort()  # Sort the list in ascending order

if len(unique_numbers) < 2:
    print("No second smallest number")
else:
    print(unique_numbers[1])  # Print the second smallest number