def decToBinary(n, bit):
    answer = ""
    for i in range(bit, -1, -1):
        k = n >> i
        if (k & 1):
            answer += "1"
        else:
            answer += "0"
    return answer


def findBit(n):
    power = 2
    bit = 0
    while n >= power:
        power *= 2
        bit += 1
    return bit


n = int(input())
answer = []
for i in range(1, n+1):
    bit = findBit(i)
    answer.append(decToBinary(i, bit))
for j in range(0, n):
    print(answer[j], end=" ")