def quicksort(arr):
    """
    Sorts an array using the quicksort algorithm.
    
    Args:
        arr: List of comparable elements to be sorted
        
    Returns:
        A new sorted list containing all elements from the input array
        
    Time Complexity: O(n log n) average case, O(n²) worst case
    Space Complexity: O(n) due to creating new lists for partitions
    """
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose pivot element (middle element of the array)
    # This is a simple pivot selection strategy
    # Note: For better performance, consider randomized pivot selection
    pivot = arr[len(arr) // 2]
    
    # Partition the array into three parts:
    # left: all elements less than the pivot
    # middle: all elements equal to the pivot (handles duplicates)
    # right: all elements greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the left and right partitions
    # Then combine: sorted_left + pivot_duplicates + sorted_right
    return quicksort(left) + middle + quicksort(right)
