# Thread Synchronization

import threading

shared_resource = 0
lock = threading.Lock()

def update_shared_resource():
    global shared_resource
    with lock:
        shared_resource += 1

threads = []

for _ in range(10):
    thread = threading.Thread(target=update_shared_resource)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Shared resource:", shared_resource)

#output
# Shared resource: 10