# Big O Notation

# Best Case: O(1)
# Average Case: O(log n)
# Worst Case: O(log n)


def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target value.
    :param arr: List of sorted elements
    :param target: The element to search for
    :return: Index of target if found, else -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target is not present in array
    return -1
