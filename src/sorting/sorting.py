# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # establish a variable for the collective length of our two inputs
    elements = len(arrA) + len(arrB)
    # create an arr of 0s that is the same length as 'elements'
    merged_arr = [0 for _ in range(elements)]
    # establish two individual counters
    a = 0
    b = 0

    # loop for the size of both arrays
    for i in range(elements):
        # if the first counter is greater than the length of the 
        # first array
        if a >= len(arrA):
            # add the content of the second array at the
            # second counter's index
            merged_arr[i] = arrB[b]
            # increment the second counter
            b += 1
        # if the second counter is greater than the length of the
        # second array
        elif b >= len(arrB):
            # add the content of the first array at the 
            # first counter's index
            merged_arr[i] = arrA[a]
            # increment the first counter
            a += 1
        # if the first array's value at the first counter's index
        # is less than the second array's value at the second counter's
        # index
        elif arrA[a] < arrB[b]:
            # add the content of the smaller value
            merged_arr[i] = arrA[a]
            # increment the first counter
            a += 1
        # if the second array's value at the second counter's index
        # is less than the first array's value at the first counter's
        # index
        else:
            # add the content of the smaller value
            merged_arr[i] = arrB[b]
            # increment the second variable
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # if the length of the array is greater than 1 
    if len(arr) > 1:
        # recursively invoke twice with 'left' being the first
        # half of the array and 'right' being the second half
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 :])

        # run the merge helper function with the 'left' and 'right'
        # halves
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

