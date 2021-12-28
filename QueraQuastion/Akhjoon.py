n1 = int(input())
d1 = input()
l1 = d1.split(" ")
n2 = int(input())
d2 = input()
l2 = d2.split(" ")
n3 = int(input())
d3 = input()
l3 = d3.split(" ")
for i in l2:
    if not l1.count(i):
        l1.append(i)
for i in l3:
    if not l1.count(i):
        l1.append(i)
n = len(l1)
print(7 - n)