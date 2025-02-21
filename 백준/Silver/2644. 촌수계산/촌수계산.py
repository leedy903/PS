import sys
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
tree = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    parent, child = map(int, input().split())
    tree[parent].append(child)
    tree[child].append(parent)

count = 0
def dfs(depth, cur_node):
    global count
    if cur_node == p2:
        count = depth
        return
    visited[cur_node] = True
    for next_node in tree[cur_node]:
        if not visited[next_node]:
            dfs(depth + 1, next_node)

dfs(0, p1)
if count == 0:
    count = -1
print(count)