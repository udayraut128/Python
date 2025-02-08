numbers = list(map(int, input().split()))

n = len(numbers)
values = numbers[0:]
mean_value = round(sum(values) / n)


print(mean_value)



