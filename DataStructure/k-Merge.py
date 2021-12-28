def mergeTwoArrays(l, r):
    ret = []
    l_in, r_in = 0, 0
    while l_in + r_in < len(l) + len(r):
        if (l_in != len(l) and
                (r_in == len(r) or
                 l[l_in] < r[r_in])):

            ret.append(l[l_in])
            l_in += 1
        else:
            ret.append(r[r_in])
            r_in += 1

    return ret


def mergeArrays(arr):
    arr_s = []
    while len(arr) != 1:
        arr_s[:] = []

        for i in range(0, len(arr), 2):
            if i == len(arr) - 1:
                arr_s.append(arr[i])

            else:
                arr_s.append(mergeTwoArrays(arr[i], arr[i + 1]))
        arr = arr_s[:]
    return arr[0]


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


n = int(input())
size, arr,  num= 0, [], []
numbers = []
for i in range(0, n):
    arr = input().split(" ")
    temp = int(arr[0])
    size += temp
    for j in range(1, temp+1):
        num.append(int(arr[j]))
    numbers.append(num)
    num = []
output = mergeArrays(numbers)
printArray(output, size)
