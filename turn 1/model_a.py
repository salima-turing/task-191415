import time
import random
import concurrent.futures

# Legacy System Function to be Tested (Simulated)
def process_iot_data(data_point):
	# Simulate processing time with a random delay
	time.sleep(random.uniform(0.1, 0.5))
	return len(data_point)

def test_scalability(num_workers=10, num_data_points=1000):
	start_time = time.time()

	# Create a list of mock data points
	data_points = [str(i) for i in range(num_data_points)]

	with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
		# Map the data points to the legacy system function for processing using executor
		results = executor.map(process_iot_data, data_points)

	total_processed = sum(results)

	end_time = time.time()
	execution_time = end_time - start_time

	print(f"Scalability Test Results:")
	print(f"-----------------------")
	print(f"Number of Workers: {num_workers}")
	print(f"Number of Data Points: {num_data_points}")
	print(f"Total Data Processed: {total_processed}")
	print(f"Execution Time: {execution_time:.2f} seconds")
	print(f"Throughput: {total_processed / execution_time:.2f} data points per second")

if __name__ == "__main__":
	test_scalability(num_workers=20, num_data_points=5000)
