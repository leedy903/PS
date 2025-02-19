import sys
input = sys.stdin.readline

n = int(input())
sequences = list(map(int, input().split()))
stack = []
ans = [-1 for _ in range(n)]

for i in range(n):
    while stack and sequences[stack[-1]] < sequences[i]:
        ans[stack.pop()] = sequences[i]
    stack.append(i)

print(*ans)