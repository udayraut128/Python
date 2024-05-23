# Multithreading in Python refers to the ability of a program to execute multiple threads (smaller units of a process) concurrently, allowing it to perform multiple tasks simultaneously. Multithreading is particularly useful for tasks that can be executed independently, such as I/O-bound or CPU-bound operations, as it can improve performance and responsiveness.


import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# Create a thread
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to finish (optional)
thread.join()

print("Thread finished.")


#output
# 0
# 1
# 2
# 3
# 4
# Thread finished.