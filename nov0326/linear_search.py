def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list of elements to search through.
    target: The value to search for in the list.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1