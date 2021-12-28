import re
string = input()
string1 = string
string1 = string1.replace("+", "-")
char = list(string)
numbers = string1.split("-")
positiveNum, negativeNum = [], []
j = 1
for i in range(len(char)):
    if char[i] == "+":
        positiveNum.append(int(numbers[j]))
        j += 1
    elif char[i] == "-":
        negativeNum.append(int(numbers[j]))
        j += 1
result = 0
resultStr = ""
if len(positiveNum) == len(negativeNum):
    positiveNum.sort()
    negativeNum.sort()
    positiveNum.reverse()
    for i in range(len(negativeNum)):
        resultStr += "+"+str(positiveNum[i])
        resultStr +="-"+str(negativeNum[i])
        result += positiveNum[i]-negativeNum[i]
print(resultStr+"="+str(result))