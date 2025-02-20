import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(N)]
dishes += dishes

window = deque()
max_sushi = 0
for i in range(k - 1):
    window.append(dishes[i])

for i in range(k - 1, N + k - 1):
    window.append(dishes[i])
    cur_dish = set(window)
    if c in cur_dish:
        max_sushi = max(max_sushi, len(cur_dish))
    else:
        max_sushi = max(max_sushi, len(cur_dish) + 1)
    window.popleft()

print(max_sushi)