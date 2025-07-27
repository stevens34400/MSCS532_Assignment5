# Quicksort Algorithm: Implementation, Analysis, and Randomization

## Overview

This project contains Python implementations of both the deterministic and randomized versions of the Quicksort algorithm, along with a performance analysis script to compare their execution times.

## Files

- `quicksort.py`: Deterministic Quicksort implementation using middle element as pivot
- `randomized_quicksort.py`: Randomized Quicksort implementation using random pivot selection
- `performance_analysis.py`: Performance benchmarking script comparing both implementations

## How to Run

### Individual Algorithm Testing
1. Clone the repository
2. Run `python quicksort.py` to test the deterministic version
3. Run `python randomized_quicksort.py` to test the randomized version

### Performance Analysis
Run the performance comparison script:
```bash
python performance_analysis.py
```

This will benchmark both algorithms on arrays of different sizes (100, 1000, 5000, 10000 elements) and display execution times for comparison.

## Algorithm Details

### Deterministic Quicksort (`quicksort.py`)
- Uses the middle element as the pivot
- Time Complexity: O(n log n) average case, O(n²) worst case
- Space Complexity: O(n)
- Handles duplicate elements efficiently

### Randomized Quicksort (`randomized_quicksort.py`)
- Uses random pivot selection to avoid worst-case scenarios
- Time Complexity: O(n log n) average case, O(n²) worst case (rare due to randomization)
- Space Complexity: O(n)
- Generally provides more consistent performance across different input distributions

## Performance Analysis

The `performance_analysis.py` script generates random arrays of varying sizes and measures the execution time of both algorithms, providing empirical data to compare their performance characteristics.
