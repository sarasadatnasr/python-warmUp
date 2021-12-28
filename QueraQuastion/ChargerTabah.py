v = input()
v1 = v.split(" ")
n = int(v1[0])
x = int(v1[1])
y = int(v1[2])
full = 0
temp = 0
charge = input()
charges = charge.split(" ")
charges1 = (int(x) for x in charge.split(" "))
minimum = int(min(charges1))
for i in range(0, n):
    temp = int(charges[i])
    if temp >= 100:
        full += 1
    else:
        while True:
            minimum -= x
            if (minimum < 0):
                break
            temp += y
            if temp >= 100:
                full += 1
                break

if full == n - 1 and minimum > 0:
    print("YES")
else:
    print("NO")