value = input()
values = value.split(" ")
n = int(values[0])
x = int(values[1])
k = int(values[2])
channels = []
for i in range(n):
  channels.append(input())
k = k % n
current = x + k
if current > n:
    current -= n
print(channels[current-1])
