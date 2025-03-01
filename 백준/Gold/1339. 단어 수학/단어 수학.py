N = int(input())
Words = [[' ', 0] for _ in range(N)]
AlphaNum = [0 for _ in range(26)]

for i in range(N):
    Words[i][0] = list(input())
    Words[i][1] = len(Words[i][0])

for i in range(N):
    WordLen = Words[i][1]
    for j in range(WordLen):
        Words[i][1] -= 1
        AlphaNum[ord(Words[i][0][j])-65] += 10**Words[i][1]

AlphaNum.sort(reverse=True)
ans = 0
for i in range(10):
    ans += AlphaNum[i]*(9-i)

print(ans)