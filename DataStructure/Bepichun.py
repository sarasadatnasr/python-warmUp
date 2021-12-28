def firstsort(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high - low) // 2;
        if ((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
            return mid
        if (x > arr[mid]):
            return firstsort(arr, (mid + 1), high, x, n)
        return firstsort(arr, low, (mid - 1), x, n)

    return -1

def quickSort(arr1, arr2, n1, n2):
    temp = [0] * n1
    visited = [0] * n1

    for i in range(0, n1):
        temp[i] = arr1[i]
        visited[i] = 0

    temp.sort()
    ind = 0
    for i in range(0, n2):
        f = firstsort(temp, 0, n1 - 1, arr2[i], n1)
        if (f == -1):
            continue

        j = f
        while (j < n1 and temp[j] == arr2[i]):
            arr1[ind] = temp[j];
            ind = ind + 1
            visited[j] = 1
            j = j + 1

    for i in range(0, n1):
        if (visited[i] == 0):
            arr1[ind] = temp[i]
            ind = ind + 1
def convertStringToAscii(arr,n):
    array = []
    for i in range(n):
        array.append(ord(arr[i]))
    return array
def convertAsciiToString(arr,n):
    array = []
    for i in range(n):
        array.append(chr(arr[i]))
    return array

#+++++++++++++++++++++++++++++++++++++++++++++++


n = int(input())
array1 = input()
array2 = input()
arr1 = array1.split(" ")
arr2 = array2.split(" ")
arr1 = convertStringToAscii(arr1, n)
arr2 = [1 , 2, 3, 4]
quickSort(arr1, arr2, n, 4)
arr1 = convertAsciiToString(arr1, n)
for i in range(0, n):
    print(arr1[i], end=" ")
print("")
for i in range(0, n):
    print(arr1[i], end=" ")
print("")
