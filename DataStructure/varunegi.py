def mergeSort(arr, n):
    temp = [0] * n
    return mainMergeSort(arr, temp, 0, n - 1)

def mainMergeSort(arr, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += mainMergeSort(arr, temp, left, mid)
        count += mainMergeSort(arr, temp, mid + 1, right)
        count += merge(arr, temp, left, mid, right)
    return count

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0

    while i <= mid and j <= right:

        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp[loop_var]

    return count


n = int(input())
numbers = []
for i in range(0, n):
    numbers.append(int(input()))
print(mergeSort(numbers, n) % 100000)