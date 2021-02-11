import time

def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return 1
    return -1;

start = time.time()

arr = [ i for i in range(100000000)]
x = 99999995
n = len(arr)

result = search(arr, n, x)
if result == -1:
    print("Element is no in the array")
else:
    print("Element is found at index", result)
    print("time taken for ", input, ":", time.time() - start)

