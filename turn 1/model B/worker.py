# worker.py
import time
import random
from app import data_queue

def process_data_queue():
    while True:
        if data_queue:
            data = data_queue.pop(0)
            # Simulate some processing time
            time.sleep(random.uniform(0.1, 0.5))
            print(f"Processed data: {data}")
        else:
            time.sleep(0.1)

if __name__ == '__main__':
    process_data_queue()
