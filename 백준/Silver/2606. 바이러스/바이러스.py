n = int(input())
m = int(input())

adj_list = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    adj_list[x-1].append(y-1)
    adj_list[y-1].append(x-1)

def dfs():
    count = -1
    stack = [0]
    visited[0] = True
    while len(stack):
        index = stack.pop()
        count += 1
        for i in range(len(adj_list[index])):
            tmp = adj_list[index][i]
            if not visited[tmp]:
                stack.append(tmp)
                visited[tmp] = True
    return count

print(dfs())