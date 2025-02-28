import sys
from collections import deque
input = sys.stdin.readline

ans = ""
happy = "happy\n"
sad = "sad\n"

def get_distance(point1, point2):
    y1, x1 = point1
    y2, x2 = point2
    return abs(y2 - y1) + abs(x2 - x1)

t = int(input())
for test_case in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    stores = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))

    visited = [False for _ in range(n)]
    possible = False

    deq = deque([home])
    while deq:
        now = deq.popleft()
        if get_distance(now, festival) <= 1000:
            possible = True
            break
        for i in range(n):
            store = stores[i]
            if not visited[i] and get_distance(now, store) <= 1000:
                deq.append(store)
                visited[i] = True
    
    if possible:
        ans += happy
    else:
        ans += sad

print(ans)