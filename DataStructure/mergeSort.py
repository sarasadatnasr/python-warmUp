def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    l = [0] * (n1)
    r = [0] * (n2)
    for i in range(0, n1):
        l[i] = arr[l + i]

    for j in range(0, n2):
        r[j] = arr[m + 1 + j]

    i, j, k = 0

    while i < n1 and j < n2:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
