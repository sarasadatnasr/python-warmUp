result, arr, i = [], [], 0
n = int(input())
while i < n:
    isSorted = True
    size = int(input())
    arr.append(int(input()))

    for j in range(1, size):
        arr.append(int(input()))
        if arr[j-1] > arr[j]:
            isSorted = False

    arr.clear()
    if isSorted:
        result.append("TIE")
    else:
        result.append("LMT")
    i += 1

for j in range(0, n):
    print(result[j])
