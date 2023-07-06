import threading
import requests
import time


def make_request():
    while True:
        response = requests.get('http://localhost:8000')
        print(response.text)
        time.sleep(1)  # Sleep for 1 second


# Spawn four threads
for _ in range(4):
    thread = threading.Thread(target=make_request)
    thread.start()
