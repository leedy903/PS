import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
target_color = [0] + list(map(int, input().rstrip().split()))
adjacency_list = defaultdict(list)
visited = [False for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().rstrip().split())
    adjacency_list[a].append(b)
    adjacency_list[b].append(a)

adjacency_list[0] = [1]

ans = 0
deq = deque([0])
visited[0] = True

while deq:
    cur_node = deq.popleft()
    for next_node in adjacency_list[cur_node]:
        if not visited[next_node]:
            if target_color[cur_node] != target_color[next_node]:
                ans += 1
            deq.append(next_node)
            visited[next_node] = True

print(ans)