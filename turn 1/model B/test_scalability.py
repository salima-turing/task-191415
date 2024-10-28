# test_scalability.py
from random import random
from app import data_queue

import pytest
import requests
import time

@pytest.fixture
def flask_app():
    from app import app
    return app

@pytest.fixture
def worker_process():
    import subprocess
    worker_process = subprocess.Popen(['python', 'worker.py'])
    yield worker_process
    worker_process.terminate()

def test_scalability(flask_app, worker_process):
    # Start the Flask app
    flask_app.run(debug=True, use_reloader=False)

    # Generate a large number of data points to simulate IoT device data
    data_points = [{'device_id': i, 'value': random.randint(1, 100)} for i in range(2)]

    # Send data to the API endpoint in batches
    batch_size = 100
    for i in range(0, len(data_points), batch_size):
        batch = data_points[i:i+batch_size]
        response = requests.post('http://localhost:5000/api/data', json=batch)
        assert response.status_code == 201

    # Wait for the worker process to finish processing all data
    time.sleep(5)

    # Assert that all data points were processed
    assert len(data_queue) == 0
