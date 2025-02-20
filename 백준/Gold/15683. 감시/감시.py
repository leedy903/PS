import sys
from copy import deepcopy
N, M = map(int, sys.stdin.readline().split())
office = []
cctvs = []

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    office.append(data)
    for j in range(M):
        if 0 < data[j] < 6:
            cctvs.append([data[j], j, i])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

def monitor_check(temp_office, sight, x, y):
    for i in sight:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                break
            if temp_office[ny][nx] == 6:
                break
            elif temp_office[ny][nx] == 0:
                temp_office[ny][nx] = 7
  
def monitor(depth, temp_office):
    global min_value

    if depth == len(cctvs):
        count = 0
        for i in range(N):
            count += temp_office[i].count(0)
        min_value = min(min_value, count)
        return

    temp = deepcopy(temp_office)
    cctv, x, y = cctvs[depth]
    for sight in mode[cctv]:
        monitor_check(temp, sight, x, y)
        monitor(depth + 1, temp)
        temp = deepcopy(temp_office)

min_value = int(1e9)
monitor(0, office)
print(min_value)