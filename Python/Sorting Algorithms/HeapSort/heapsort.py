# Time Complexity: O(nlogn)
# Space Complexity: O(1)

def heapify(arr, n, i):
    """
    Helper function to maintain the heap property of a subtree rooted at index i.
    :param arr: List of elements
    :param n: Size of the heap
    :param i: Root index of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Heapify the root
        heapify(arr, n, largest)

def heapsort(arr):
    """
    Perform heapsort on the given array.
    :param arr: List of elements to sort
    :return: Sorted list
    """
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr
