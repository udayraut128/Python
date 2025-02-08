numbers = list(map(int, input().split()))
seen = set()
unique_numbers = []

for num in numbers:
    if num % 2 == 0:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    else:
        unique_numbers.append(num)

print(" ".join(map(str, unique_numbers)))