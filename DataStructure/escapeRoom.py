cd1 = input()
cd2 = input()
cd1 = cd1.split()
cd2 = cd2.split()
disk1, disk2 = [], []
yekan, dahgan, sadgan, num = 0, 0, 0, 0
possible = False
for i in range(0, 5):
    disk1.append(int(cd1[i]))
    disk2.append(int(cd2[i]))
disk1 += disk1
disk2 += disk2

for i in range(0, 5):
    for j in range(0, 5):
         sadgan = ((disk1[i] + disk2[j]) % 10) * 100
         dahgan = ((disk1[i + 1] + disk2[j + 1]) % 10) * 10
         yekan = ((disk1[i + 2] + disk2[j + 2]) % 10)
         num = sadgan + dahgan + yekan
         if num % 6 == 0:
            possible = True

if possible:
    print('Boro joloo :)')
else:
    print('Gir oftadi :(')
