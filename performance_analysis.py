# Performance Analysis Script for Quicksort Algorithms
# This script compares the performance of deterministic vs randomized quicksort
# implementations across different input sizes.

import time
import random
from quicksort import quicksort
from randomized_quicksort import randomized_quicksort

def benchmark(sort_func, arr):
    """
    Benchmark a sorting function by measuring its execution time.
    
    Args:
        sort_func: The sorting function to benchmark
        arr: The array to sort (will be modified in-place)
    
    Returns:
        float: Execution time in seconds
    """
    start = time.time()
    sort_func(arr)  # Sort the array in-place
    return time.time() - start

# Test different input sizes to analyze performance scaling
# Small sizes for quick testing, larger sizes to see performance differences
sizes = [100, 1000, 5000, 10000]

# Run benchmarks for each input size
for size in sizes:
    # Generate a random array with values between 0 and 10000
    # This creates a realistic test case with potential duplicates
    arr = [random.randint(0, 10000) for _ in range(size)]
    
    print(f"Size: {size}")
    
    # Benchmark deterministic quicksort (pivot selection strategy may vary)
    # Using arr[:] creates a copy to ensure fair comparison
    print("Deterministic Quicksort:", benchmark(quicksort, arr[:]))
    
    # Benchmark randomized quicksort (random pivot selection)
    # Using arr[:] creates a copy to ensure fair comparison
    print("Randomized Quicksort:", benchmark(randomized_quicksort, arr[:]))
    
    print("-" * 40)  # Separator for readability
