def find(num1, num2, num3):
    number = []
    number.append(num1)
    number.append(num2)
    number.append(num3)
    for i in range(1, 5):
        if i not in number:
            return i

