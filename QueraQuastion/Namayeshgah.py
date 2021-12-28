n = int(input())
arr = []
arr.append("########.......########")
arr.append("#ghorfe1..............#")
arr.append("#ghorfe1.......ghorfe2#")
arr.append("#ghorfe3..............#")
arr.append("#ghorfe3.......ghorfe4#")
arr.append("#ghorfe5..............#")
arr.append("#ghorfe5.......ghorfe6#")
arr.append("#ghorfe7..............#")
arr.append("#ghorfe7.......ghorfe8#")
arr.append("#.....................#")
i = 0
print(arr[0])
if n == 0:
    print(arr[9])
    print(arr[0])
    print(arr[9])
    print(arr[0])
    print(arr[9])
    print(arr[0])
    print(arr[9])

elif n == 1:
    print(arr[1])
    for i in range(0, 3):
        print(arr[0])
        print(arr[9])
elif n == 2:
    print(arr[2])
    for i in range(0, 3):
        print(arr[0])
        print(arr[9])
elif n == 3:
    print(arr[2])
    print(arr[0])
    print(arr[3])
    for i in range(0, 2):
        print(arr[0])
        print(arr[9])
elif n == 4:
    print(arr[2])
    print(arr[0])
    print(arr[4])
    for i in range(0, 2):
        print(arr[0])
        print(arr[9])
elif n == 5:
    print(arr[2])
    print(arr[0])
    print(arr[4])
    print(arr[0])
    print(arr[5])
    for i in range(0, 1):
        print(arr[0])
        print(arr[9])
elif n == 6:
    print(arr[2])
    print(arr[0])
    print(arr[4])
    print(arr[0])
    print(arr[6])
    for i in range(0, 1):
        print(arr[0])
        print(arr[9])
elif n == 7:
    print(arr[2])
    print(arr[0])
    print(arr[4])
    print(arr[0])
    print(arr[6])
    print(arr[0])
    print(arr[7])

elif n == 8:
    print(arr[2])
    print(arr[0])
    print(arr[4])
    print(arr[0])
    print(arr[6])
    print(arr[0])
    print(arr[8])

print("#######################")