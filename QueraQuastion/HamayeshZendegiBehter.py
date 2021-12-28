inputStr=input()
str=[]
str=inputStr.split(" ")
x=int(str[0])
y=int(str[1])
if y<=10:
    row=y
    column=11-x
    print("Right",column,row)
else:
    row =21 - y
    column =11-x
    print("Left",column,row)

