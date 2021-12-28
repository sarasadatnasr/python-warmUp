string = input()
num = string.split(" ")
a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])
m = int(num[4])
n1 = c/a
n2 = d/b
m1 = (c*m)+a
m2 = (d*m)+b
if c > d and m1 >= m2:
    print("Eyval baba!")

elif c < d and m1 <= m2:
    print("Eyval baba!")

else:
    print("Naaa, eshtebahe!")
