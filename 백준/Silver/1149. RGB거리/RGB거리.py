import sys

N = int(sys.stdin.readline())
costs = [None for _ in range(N)]

for i in range(N):
    costs[i] = list(map(int, sys.stdin.readline().split()))


for i in range(1, N):
    for j in range(3):
        current_cost = costs[i - 1][:]
        current_cost.pop(j)
        costs[i][j] += min(current_cost)

print(min(costs[-1]))