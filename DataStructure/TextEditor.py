arr = list(input())
result = []
finalStr = ""
pointer, cursor = 0, 0

while pointer < len(arr):
    if arr[pointer] == "<":
        if cursor > 0:
            cursor -= 1

    elif arr[pointer] == ">":
        if cursor < len(result):
            cursor += 1

    elif arr[pointer] == "-":
        if len(result) > 0 and cursor > 0:
            del result[cursor-1]
            cursor -= 1

    else:
        result.insert(cursor, arr[pointer])
        cursor += 1

    pointer += 1

for i in range(len(result)):
    finalStr += result[i]

if finalStr == " " or finalStr == "":
    print(-1)
else:
    print(finalStr)


#<a>-<b>-<c>

