STRING = input().split('-')
for i in range(len(STRING)):
    num = STRING[i].split('+')
    temp = 0
    for j in range(len(num)):
        temp += int(num[j])
    STRING[i] = temp

ans = STRING[0]
for i in range(1, len(STRING)):
    ans -= STRING[i]
print(ans)