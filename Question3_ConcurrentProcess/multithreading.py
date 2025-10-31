# multithreading
import threading # to create thread
import time
from factorial import factorial

# store results of factorials
results = {}

# factorial functions 
def compute_factorial(n, key):
    start = time.perf_counter_ns()
    results[key] = factorial(n)
    end = time.perf_counter_ns()
    return end - start

# function to calculate time taken
def run_thread(rounds=10):
    times = []
    for r in range(rounds):
        threads = []
        results.clear()

        t1_start = time.perf_counter_ns()

        # Create 3 threads (50!, 100!, and 200!)
        threads.append(threading.Thread(target=compute_factorial, args=(50, "50")))
        threads.append(threading.Thread(target=compute_factorial, args=(100, "100")))
        threads.append(threading.Thread(target=compute_factorial, args=(200, "200")))

        # Start threads
        for t in threads:
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()
        t2_end = time.perf_counter_ns()

        # calculate total time taken
        total_time = t2_end - t1_start
        times.append(total_time)
        print(f"Round {r+1}: {total_time} ns")

    # calculate total time
    total_time = sum(times)
    print(f"\nTotal Time (10 rounds): {total_time} ns")

    # calculate average time
    avg_time = sum(times) / len(times)
    print(f"Average Time (Threaded): {avg_time:.2f} ns")

if __name__ == "__main__":
    run_thread()
