def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


# code for merge sort

def mergeSort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x) // 2
        a = mergeSort(x[:middle])
        b = mergeSort(x[middle:])
        return merge(a, b)
input1 = input()
input2 = input()
inputs = input1.split(" ")
numbers = input2.split(" ")
n = int(inputs[0])
k = int(inputs[1])
arr = []
result = 0
for i in range(0, n):
    arr.append(int(numbers[i]))
arr = mergeSort(arr)
for i in range(0, n-k):
    result += arr[i]
print(result)