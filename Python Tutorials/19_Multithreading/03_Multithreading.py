# Thread Pooling

from concurrent.futures import ThreadPoolExecutor

def task(num):
    return num * num

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(10))

print(list(results))

#output
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]