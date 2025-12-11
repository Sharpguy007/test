#QUESTION 1
def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.

    Args:
        arr (list): The list of comparable elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them.
        swapped = False
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1.
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Optimization: If no two elements were swapped by inner loop, then the list is sorted
        if not swapped:
            break
    
    return arr

list_to_sort = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(list_to_sort.copy()) # Use .copy() to keep the original list intact
print(f"1. Bubble Sort Result: {sorted_list}")


QUESTION 2
def find_intersection(arr1, arr2):
    """
    Finds the intersection of two arrays (elements common to both).

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: A list containing the common elements (the intersection).
    """
    # Convert both lists to sets
    set1 = set(arr1)
    set2 = set(arr2)
    
    # Use the set intersection operation (&)
    # The result is a set, so convert it back to a list
    intersection_set = set1 & set2
    
    return list(intersection_set)

# Example Usage
array_a = [1, 2, 3, 4, 5]
array_b = [4, 5, 6, 7, 8]
intersection = find_intersection(array_a, array_b)
print(f"2. Intersection of {array_a} and {array_b}: {intersection}")

# Alternative using set.intersection() method
array_c = [10, 20, 30]
array_d = [30, 40, 50, 10]
intersection_alt = list(set(array_c).intersection(set(array_d)))
print(f"   Alternative Intersection: {intersection_alt}")


Question 3
def rotate_array_right(arr, k):
    """
    Rotates an array to the right by k steps.

    Args:
        arr (list): The list to be rotated.
        k (int): The number of steps to rotate to the right.

    Returns:
        list: The rotated list.
    """
    n = len(arr)
    if n == 0:
        return []
    
    # Handle cases where k is larger than the array length (n)
    # The effective rotation is k % n
    effective_k = k % n
    
    # Python Slicing Technique:
    # 1. Take the last 'effective_k' elements: arr[n - effective_k:]
    # 2. Take the first 'n - effective_k' elements: arr[:n - effective_k]
    # 3. Concatenate them: [Last k elements] + [First n-k elements]
    rotated_arr = arr[n - effective_k:] + arr[:n - effective_k]
    
    return rotated_arr

# Example Usage
original_array = [1, 2, 3, 4, 5, 6, 7]
steps_to_rotate = 3
rotated = rotate_array_right(original_array, steps_to_rotate)
print(f"3. Array {original_array} rotated right by {steps_to_rotate} steps: {rotated}")

# Example with k > n
original_array_2 = [10, 20, 30]
steps_to_rotate_2 = 4
rotated_2 = rotate_array_right(original_array_2, steps_to_rotate_2)
print(f"   Array {original_array_2} rotated right by {steps_to_rotate_2} steps: {rotated_2}") 