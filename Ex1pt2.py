import time


def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2;

        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


start = time.time()
# Driver Code
arr = [i for i in range(100000)]
x = 9999

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
    print("time taken for ", input, ":", time.time() - start)
else:
    print("Element is not present in array")
