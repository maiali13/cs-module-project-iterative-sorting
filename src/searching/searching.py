def linear_search(arr, target):
    """
    Given a set of data, traverse the dataset one item at a time until either you find the item you are looking for 
    OR check every item in the set and verify the item you are looking for is not there.
    """
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found
    #O(n)

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    """
    First, there is a precondition that the set of data you are searching is already sorted (alphabetically, numerically, etc). 
    Then, the steps to search are:
    -Compare the item in the middle of the data set to the item we are searching for.
        If it is the same, stop. We found it and are done!
        Else, if the item we are searching for is LESS than the item in the middle:
            Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
        Else, the item we are searching for is GREATER than the item in the middle:
            Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.
    """
    low = 0
    high = len(arr)

    while high > low:
        mid = (low + high) // 2
        if arr[mid] == target:
            # Found!!
            return mid

        if arr[mid] > target:
            # we're too high, search lower half.
            high = mid

        elif arr[mid] < target:
            # we're too low, search upper half.
            low = mid + 1


    return -1  # not found
    #O(n log(n))