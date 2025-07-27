import random

def randomized_quicksort(arr):
    """
    Sorts an array using the randomized quicksort algorithm.
    
    This implementation uses a divide-and-conquer approach with random pivot selection
    to achieve O(n log n) average time complexity. The randomization helps avoid
    worst-case scenarios that can occur with deterministic pivot selection.
    
    Args:
        arr: List of comparable elements to be sorted
        
    Returns:
        List: A new sorted list containing all elements from the input array
        
    Time Complexity:
        - Average case: O(n log n)
        - Worst case: O(n²) (rare due to randomization)
        - Space complexity: O(n) due to creating new lists
    """
    # Base case: arrays of length 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr
    
    # Randomly select a pivot element to avoid worst-case scenarios
    # This helps achieve better average performance compared to always
    # choosing the first or last element
    pivot = random.choice(arr)
    
    # Partition the array into three parts:
    # - left: elements smaller than the pivot
    # - middle: elements equal to the pivot (handles duplicates efficiently)
    # - right: elements larger than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the left and right partitions, then combine
    # The middle partition is already sorted (all elements are equal)
    return randomized_quicksort(left) + middle + randomized_quicksort(right)
