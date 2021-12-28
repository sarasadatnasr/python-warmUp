def customSort(first, second):
    freq = {}
    for i in first:
        freq[i] = freq.get(i, 0) + 1
    index = 0
    for i in second:
        n = freq.setdefault(i, 0)
        for _ in range(n):
            first[index] = i
            index = index + 1
        freq.pop(i)
    for key in sorted(freq.keys()):
        count = freq.get(key)
        while count:
            first[index] = key
            count = count - 1
            index = index + 1


def toInt(arr, n):
    temp = []
    for i in range(n):
        temp.append(int(arr[i]))
    return temp


string = input().split(" ")
n1 = int(string[0])
n2 = int(string[1])
array1 = input()
array2 = input()
arr1 = array1.split(" ")
arr2 = array2.split(" ")
first = toInt(arr1, n1)
second = toInt(arr2, n2)
customSort(first, second)
for i in range(0, n1):
    print(first[i], end=" ")
print("")


