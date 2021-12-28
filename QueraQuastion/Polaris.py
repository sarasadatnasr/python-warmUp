string = input()
string = string.lower()
myList = ['a', 'b', "c", "d", "e", "f", "g", "h", "i", "j", "k",
          "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

k = 0
for i in myList:
    if string.count(i) > 0:
        k += 1
    
    else:
        print("NO")
        break
if k == 26:
    print("YES")
