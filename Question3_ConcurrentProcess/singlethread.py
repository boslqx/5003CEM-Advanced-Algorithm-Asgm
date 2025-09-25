import threading
import time
from factorial import factorial

# simpler version without thread
def run_single(rounds=10):
    times = []
    for r in range(rounds):
        t1_start = time.perf_counter_ns()

        factorial(50)
        factorial(100)
        factorial(200)

        t2_end = time.perf_counter_ns()
        total_time = t2_end - t1_start
        times.append(total_time)
        print(f"Round {r+1}: {total_time} ns")

    # calculate total time
    total_time = sum(times)
    print(f"\nTotal Time (10 rounds): {total_time} ns")

    # calculate avg time
    avg_time = sum(times) / len(times)
    print(f"Average Time (Single-threaded): {avg_time:.2f} ns")

if __name__ == "__main__":
    run_single()
