import re


def isValid(username):
    regex = re.compile('[_#$*]')
    if regex.search(username) == None:
        valid = True
    else:
        valid = False
    return valid


result = []
idUser = {}
userValue = {}
n = int(input())
for i in range(n):
    string = input().split(" ")
    order = string[0]
    other = string[1]
    # first request
    if order == "1":
        parts = other.split(":")
        ip = parts[0]
        username = parts[1]
        if isValid(username):
            idUser[ip] = username
            userValue[ip] = 0
        else:
            result.append("invalid username")
    # second request
    elif order == "2":
        parts = other.split(":")
        debtorID = parts[0]
        creditorName = parts[1]
        value = int(parts[2])
        userValue[debtorID] = userValue.get(debtorID) - value
        creditorID = list(idUser.keys())[list(idUser.values()).index(creditorName)]
        userValue[creditorID] = userValue.get(creditorID) + value
    # third request
    elif order == "3":
        parts = other.split(":")
        ip = parts[0]
        result.append(userValue[ip])

for i in range(len(result)):
    print(result[i])
