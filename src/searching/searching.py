# TO-DO: Implement a recursive implementation of binary search
def binary_search(list, target, start, end):
    # Your code here
    # give the recursion a way to end, if it reaches this point
    # target is not in the set
    if start > end:
        return -1
    # until then
    else:
        # establish a midpoint, start + end // 2
        midpoint = (start + end) // 2

        # if the midpoint is the target, return the midpoint
        if list[midpoint] == target:
            return midpoint
        # if the target is smaller than the midpoint, we're going to
        # run binary search but with none of the values greater than
        # the midpoint because they can be ruled out
        elif list[midpoint] > target:
            return binary_search(list, target, start, (midpoint - 1))
        # if the target is greater than the midpoint, we're going to
        # run binary search but with none of the values smaller than
        # the midpoint because they can be ruled out
        else:
            return binary_search(list, target, end, (midpoint + 1))


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
