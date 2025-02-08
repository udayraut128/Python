numbers = list(map(int, input().split()))
n = len(numbers)
reversed_numbers = numbers[::-1]

new_list = []
for i in range(n):
    if i % 2 == 0:
        new_list.append(numbers[i] + reversed_numbers[i])
    else:
        new_list.append(numbers[i])

print(" ".join(map(str, new_list)))