row1 = input()
row2 = input()
row3 = input()
row4 = input()
col1 = []
col2 = []
col3 = []
col4 = []
column1 = row1.split(" ")
column2 = row2.split(" ")
column3 = row3.split(" ")
column4 = row4.split(" ")
for i in range(3):
    col1.append(int(column1[i]))

for i in range(3):
    col2.append(int(column2[i]))

for i in range(3):
    col3.append(int(column3[i]))

for i in range(0, len(column4)):
    col4.append(int(column4[i]))

maximum = []
maximum.append(max(col1))
maximum.append(max(col2))
maximum.append(max(col3))
maximum.append(max(col4))
maxi = max(maximum)

for i in range(4):
    if maxi == maximum[i]:
        print(i+1)





