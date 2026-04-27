import sys
from collections import deque
input = sys.stdin.readline

N, M, fuel = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]
taxi = list(map(int, input().strip().split()))
passengers = []
destinations = []
visited = [False for _ in range(M)]

for _ in range(M):
    py, px, dy, dx = map(int, input().strip().split())
    passengers.append([py - 1, px - 1])
    destinations.append([dy - 1, dx - 1])


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def get_nearest_passenger():
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]

    deq = deque([taxi])
    dist[taxi[0]][taxi[1]] = 0

    while deq:
        y, x = deq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if matrix[ny][nx] != 1 and dist[ny][nx] > dist[y][x] + 1:
                    dist[ny][nx] = dist[y][x] + 1
                    deq.append([ny, nx])
    
    rank = []
    for i in range(M):
        py, px = passengers[i][0], passengers[i][1]
        if not visited[i]:
            rank.append((dist[py][px], py, px, i))
    
    rank.sort(key=lambda x : (x[0], x[1], x[2]))

    return rank[0]

def get_destination_distance(destination):
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    
    deq = deque([taxi])
    dist[taxi[0]][taxi[1]] = 0

    while deq:
        y, x = deq.popleft()

        if y == destination[0] and x == destination[1]:
            return dist[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if matrix[ny][nx] != 1 and dist[ny][nx] > dist[y][x] + 1:
                    dist[ny][nx] = dist[y][x] + 1
                    deq.append([ny, nx])
    return float('inf')

taxi = [taxi[0] - 1, taxi[1] - 1]
for _ in range(M):
    dist, py, px, pid = get_nearest_passenger()

    if dist <= fuel:
        taxi = [py, px]
        visited[pid] = True
        fuel -= dist
    else:
        fuel = -1
        break

    destination = destinations[pid]
    dist = get_destination_distance(destination)
    
    if dist <= fuel:
        taxi = [destination[0], destination[1]]
        fuel += dist
    else:
        fuel = -1
        break

print(fuel)
