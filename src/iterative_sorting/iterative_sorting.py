# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    """
    Start with current index = 0
    For all indices EXCEPT the last index:
        a. Loop through elements on right-hand-side of current index and find the smallest element
        b. Swap the element at current index with the smallest element found in above loop
    arr = list of sortable elements
    """
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        smallest_val = arr[i]
        for n in range(i, len(arr)):
            if arr[n] < smallest_val:
                smallest_index = n
                smallest_val = arr[n]

        # TO-DO: swap
        if cur_index != smallest_index:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    """
    Loop through your array
    Compare each element to its neighbor
    If elements in wrong position (relative to each other, swap them)
    If no swaps performed, stop. 
    Else, go back to the element at index 0 and repeat step 1.

    """
    for x in range(0, len(arr) - 1):
        for y in range(0, len(arr) - (x + 1)):
            if arr[y] > arr[y + 1]:
                temp = arr[y]
                arr[y] = arr[y + 1]
                arr[y + 1] = temp

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
