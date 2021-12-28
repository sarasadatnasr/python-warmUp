arr = []
time = []
diction = dict
n = int(input())
for i in range(0,n):
    arr.append(input())
    temp = arr[i].split(" ")
    if temp[0] == "DEP":
        value = int(temp[1])
    elif temp[0] == "WIT":
        if temp[0] == "OK":
            value = int(temp[1])*-1
    time = temp[2].split(":")
    nTime=(int(time[0])*60)+int(time[1])
    diction.update(nTime, str(value))
print(diction)


