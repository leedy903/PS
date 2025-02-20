import sys

input = sys.stdin.readline

N, M, L, K = map(int, input().split())
stars = [list(map(int, input().strip().split())) for _ in range(K)]

answer = K
for tx, _ in stars:
    for _, ty in stars:
        covered = 0
        for sx, sy in stars:
            if tx <= sx <= tx + L and ty <= sy <= ty + L:
                covered += 1
        answer = min(answer, K - covered)
print(answer)