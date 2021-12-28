k = int(input())
bank = {'ips': [], 'usernames' : [], 'monies' : []}
for i in range(k):
    inp = input()
    if inp[0] == '1':
        index = inp.find(':')
        if inp[index+1:].isalnum():

            bank['usernames'].append(inp[index+1:])
            bank['ips'].append(inp[2:index])
            bank['monies'].append(int(0))
        else:
            print('invalid username')

    if inp[0] == '2':
        index1 = inp.find(':')
        per1 = bank['ips'].index(inp[2:index1])
        str = inp[: index1] + inp[index1 + 1::]
        index2 = str.find(':')
        money = int(str[index2+1:])
        per2 = bank['usernames'].index(str[index1:index2])
        bank['monies'][per1] -= money
        bank['monies'][per2] += money

    if inp[0] == '3':
        per = inp[2:]
        index = bank['ips'].index(per)
        print(bank['monies'][index])