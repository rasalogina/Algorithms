def integerSums(n):
    value = 0
    while (n>0):
        value += n % 10
        n = n //10

    return value

def sortArray(arr, n):
    vp = []
    for i in range(n):
        vp.append([integerSums(arr[i]), arr[i]])

    vp.sort()

    for i in range(len(vp)):
        print(vp[i][1], end=" ")

    # Driver code


if __name__ == "__main__":
    N = [28, 1000, 36, 48, 2736]
    n = len(N)
    sortArray(N, n)


