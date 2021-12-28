import math
v=input()
v1=v.split(" ")
n=int(v1[0])
k=int(v1[1])
number=[]
result=0
jar=0
numbers=input()
number=numbers.split(" ")
for i in range (n):
    result+=int(number[i])

jar=math.ceil(result/k)
print(n-jar)