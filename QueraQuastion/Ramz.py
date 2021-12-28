n = int(input())
secret = input()
digit = secret.split()
n = len(digit)
result = 0
for i in range(0, n):
    string = input()
    size = len(string)
    position = string.find(digit[i])
    if position > size/2:
        result += (size-position)
    else:
        result += position
print(result)