import sys
N, M, H = map(int, sys.stdin.readline().split())
# True: horizontal line, False: Empty
horizontal = [[False] * (N - 1) for _ in range(H)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    horizontal[a - 1][b - 1] = True

ans = 4

def add_horizontal(cnt, x, y):
    global ans
    if isCorrect():
        ans = min(cnt, ans)
        return
    elif cnt == 3 or ans <= cnt:
        return
    for i in range(y, N - 1):
        if i == y:
            k = x
        else:
            k = 0
        for j in range(k, H):
            if horizontal[j][i] or (i > 0 and horizontal[j][i - 1]) or (i < N - 2 and horizontal[j][i + 1]):
                continue
            else:
                horizontal[j][i] = True
                add_horizontal(cnt + 1, j + 1, i)
                horizontal[j][i] = False 
    return

def isCorrect():
    for i in range(N):
        x = i
        for j in range(H):
            if x < N - 1 and horizontal[j][x]:
                x += 1
            elif x > 0 and horizontal[j][x - 1]:
                x -= 1
        if x != i:
            return False
    return True

add_horizontal(0, 0, 0)
print(ans if ans < 4 else -1)