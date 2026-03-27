import sys
input = sys.stdin.readline

N = int(input())
friends = [list(input().strip()) for _ in range(N)]

answer = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue

        if friends[i][j] == 'Y':
            cnt += 1
            continue

        for k in range(N):
            if friends[i][k] == 'Y' and friends[k][j] == 'Y':
                cnt += 1
                break
    answer = max(answer, cnt)

print(answer)
