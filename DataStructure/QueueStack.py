queue, stack, arr, answer, tempS, tempQ = [], [], [], [], 0, 0
inputValue = input().split(" ")
inputArray = input().split(" ")
n = int(inputValue[0])
m = int(inputValue[1])
queue.append(0)
stack.append(0)

for i in range(n):
    arr.append(int(inputArray[i]))

for i in range(m):
    tempS += arr[i]
    tempQ += arr[n-i-1]
    stack.append(tempS)
    queue.append(tempQ)
for i in range(1, m+1):
    answer.append(stack[i] + queue[m-i])
print(max(answer))



