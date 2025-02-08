import requests
import threading

def download_file(url, filename):
    print(f"Downloading {url} to {filename}")
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename} successfully")
    else:
        print(f"Failed to download {url}")

# List of URLs and corresponding filenames
urls = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg"
]
filenames = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Create and start threads for downloading each file
threads = []
for url, filename in zip(urls, filenames):
    thread = threading.Thread(target=download_file, args=(url, filename))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All files downloaded successfully")
