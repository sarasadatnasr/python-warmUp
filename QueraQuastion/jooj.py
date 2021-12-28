j = 0
n = int(input())
inn = input()
arr = inn.split(" ")
if n==1 or n==2:
    print("Bah Bah! Ajab jooji!")
else:
    for i in range(1, n-1):
        if int(arr[i]) > int(arr[i - 1]) and int(arr[i]) > int(arr[i + 1]):
             print("Ey baba :(")
             break

        else:
             j += 1

    if(j == n-2):
        print("Bah Bah! Ajab jooji!")
