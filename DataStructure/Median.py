def binarySearch(arr, item, low, high):
    if low < high:
        if item > arr[low]:
            return low + 1
        else:
            return low
    mid = (low + high) / 2
    if item == arr[mid]:
        return mid + 1
    if item > arr[mid]:
        return binarySearch(arr, item, mid + 1, high)
    return binarySearch(arr, item, low, mid - 1)


def printMedian(arr, n):
    i, j, pos, num = 0, 0, 0, 0
    count = 1
    print(arr[0])
    for i  in range(1 ,n):
        median = 0.0
        j = i - 1
        num = arr[i]

        pos = binarySearch(arr, num, 0, j)

        while j >= pos:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num

        count += 1

        if count % 2 != 0:
            median = arr[count / 2]
        else:
            median = (arr[(count / 2) - 1] + arr[count / 2])/ 2
        print(i + 1, median)



n = int(input())
string = input().split(" ")
arr, mid, temp = [], [], []
for i in range(0, n):
    arr.append(int(string[i]))


for i in range(n):
    print("{:.1f}".format(mid[i]))