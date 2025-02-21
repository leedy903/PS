'''Baekjoon 1260, dfs, bfs with adj_list'''
from queue import Queue
N, M, V = map(int, input().split())

LIST = [[] for _ in range(N)]
VISITED = [False for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    LIST[x-1].append(y-1)
    LIST[y-1].append(x-1)

for i in range(N):
    LIST[i].sort()

def dfs(index):
    '''dfs function'''
    global N, LIST, VISITED
    VISITED[index] = True
    print(index + 1, end=" ")
    for i in range(len(LIST[index])):
        tmp = LIST[index][i]
        if not VISITED[tmp]:
            dfs(tmp)
    return

def bfs(index):
    ''' bfs function '''
    global N, LIST, VISITED
    que = Queue()
    que.put(index)
    VISITED[index] = True
    while not que.empty():
        index = que.get()
        print(index + 1, end=" ")
        for i in range(len(LIST[index])):
            tmp = LIST[index][i]
            if not VISITED[tmp]:
                VISITED[tmp] = True
                que.put(tmp)

dfs(V - 1)
VISITED = [False for _ in range(N)]
print()
bfs(V - 1)