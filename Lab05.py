
def integerSums(n):
    sum = 0;
    while (n > 0):
        sum += n % 10;
        n = n // 10;

    return sum;


def sortArr(arr, n):
    vp = [];

    # Inserting digit sum with element
    # in the vector pair
    for i in range(n):
        vp.append([integerSums(arr[i]), arr[i]]);

        # Quick sort the vector, this will
    # sort the pair according to sum
    # of the digits of elements
    vp.sort()

    # Print the sorted vector content
    for i in range(len(vp)):
        print(vp[i][1], end=" ");

    # Driver code


if __name__ == "__main__":
    arr = [28, 1000, 36, 48, 2736];
    n = len(arr);
    sortArr(arr, n);

    # This code is contributed by Ryuga