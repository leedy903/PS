import sys
H, W, X, Y = map(int, sys.stdin.readline().split())
A = [[0] * W for _ in range(H)]
B = [list(map(int, sys.stdin.readline().split())) for _ in range(H + X)]

for i in range(H):
    for j in range(W):
        A[i][j] = B[i][j]

for i in range(H - X):
    for j in range(W - Y):
        A[X + i][Y + j] = B[X + i][Y + j] - A[i][j]

for i in range(H):
    for j in range(W):
        print(A[i][j], end=" ")
    print()