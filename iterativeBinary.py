import time


def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    mid = 0

    while l <= r:

        mid = (r + l) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            r = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


start = time.time()

# Test array
arr = [i for i in range(100000)]
x = 9999

# Function call
result = binary_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
    print("time taken for ", input, ":", time.time() - start)
else:
    print("Element is not present in array")
