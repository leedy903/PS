import sys
from collections import deque

def spring_to_summer() -> None:
    global trees, nutrient_of_land
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if nutrient_of_land[i][j] >= trees[i][j][k]:
                    nutrient_of_land[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, len(trees[i][j])):
                        nutrient_of_land[i][j] += trees[i][j].pop()//2
                    break
    return

def autumn_to_winter() -> None:
    global trees
    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:
                if  tree % 5 == 0:
                    for k in range(8):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if nc >= 0 and nr >= 0 and nc < N and nr < N:
                            trees[nr][nc].appendleft(1)
    
            nutrient_of_land[i][j] += A[i][j]
    return

if __name__ == "__main__":
    dc = [-1, -1, 0, 1, 1, 1, 0, -1]
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    N, M, K = map(int, sys.stdin.readline().split())
    A = [[] for _ in range(N)]
    nutrient_of_land = [[5 for _ in range(N)] for _ in range(N)]
    trees = [[deque() for _ in range(N)] for _ in range(N)]
    for i in range(N):
        A[i] = list(map(int, sys.stdin.readline().split()))

    for _ in range(M):
         r, c, year = map(int, sys.stdin.readline().split())
         trees[r - 1][c - 1].append(year)

    for _ in range(K):
        spring_to_summer()
        autumn_to_winter()
    
    number_of_trees = 0
    for i in range(N):
        for j in range(N):
            number_of_trees += len(trees[i][j])
    print(number_of_trees)