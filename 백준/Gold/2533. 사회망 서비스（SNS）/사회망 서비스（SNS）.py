import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(node):
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child])

n = int(input())
tree = [[] for _ in range(n + 1)]
dp = [[0, 1] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)
print(min(dp[1]))