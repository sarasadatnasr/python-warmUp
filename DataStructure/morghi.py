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


n = int(input())
numbers = []
for i in range(0, n):
    numbers.append(int(input()))
numbers = mergeSort(numbers)
#print(numbers)
i = 1
j = 0
temp = 0
for k in range(0, len(numbers)):
#print(i, numbers[k])
    temp += abs(i-numbers[k])
    i += 1
print(temp)




