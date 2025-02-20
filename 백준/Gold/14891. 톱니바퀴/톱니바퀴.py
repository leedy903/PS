import sys
from collections import deque

input = sys.stdin.readline

gears = [deque([int(pole) for pole in list(input())[:-1]]) for _ in range(4)]
k = int(input())
works = [list(map(int, input().split())) for _ in range(k)]
visit = [False for _ in range(4)]
queue = []

def make_queue(gear_id, direction):
    queue.append([gear_id, direction])
    visit[gear_id] = True
    if gear_id - 1 > -1 and not visit[gear_id - 1]:
        if gears[gear_id - 1][2] != gears[gear_id][6]:
            make_queue(gear_id - 1, direction * (-1))
    if gear_id + 1 < 4 and not visit[gear_id + 1]:
        if gears[gear_id][2] != gears[gear_id + 1][6]:
            make_queue(gear_id + 1, direction * (-1))
    
for work in works:
    gear_id, direction = work
    visit = [False for _ in range(4)]
    queue = []
    make_queue(gear_id - 1, direction)
    for gear_id, direction in queue:
        gears[gear_id].rotate(direction)

score = sum([gear[0] * (2 ** i) for i, gear in enumerate(gears)])
print(score)