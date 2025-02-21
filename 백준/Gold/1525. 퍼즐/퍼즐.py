import sys
from collections import deque

input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

puzzle = ""
for i in range(3):
    puzzle += "".join(input().split())

history = {puzzle:0}
deq = deque([puzzle])

def bfs():
    while deq:
        puzzle = deq.popleft()
        count = history[puzzle]
        zero = puzzle.index('0')

        if puzzle == "123456780":
            return count
        
        y = zero // 3
        x = zero % 3

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 3 and 0 <= nx < 3:
                new_zero = ny * 3 + nx
                puzzle_list = list(puzzle)
                puzzle_list[zero], puzzle_list[new_zero] = puzzle_list[new_zero], puzzle_list[zero]
                new_puzzle = "".join(puzzle_list)

                if new_puzzle not in history:
                    history[new_puzzle] = count + 1
                    deq.append(new_puzzle)
    
    return -1

ans = bfs()
print(ans)