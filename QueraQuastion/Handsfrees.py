hand1 = input()
hand2 = input()
hands1 = hand1.split(" ")
hands2 = hand2.split(" ")
possible = False
if hands1[0] == hands1[1]:
    print("YES")
elif hands2[0] == hands2[1]:
    print("YES")
elif hands1[0] == hands2[1]:
    print("YES")
elif hands1[1] == hands2[0]:
    print("YES")
else:
    print("NO")