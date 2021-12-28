string = []
number = []
j = 0
for i in range(0, 5):
    print(i)
    string.append(input())
    if string[i].find("MOLANA") or string[i].find("HAFEZ"):
        number.append(str(i + 1))
        j += 1
        
for i in range(5):
    if number[i] != "0" and j > 0:
        print(number[i])
    elif j == 0:
        print("NOT FOUND!")
