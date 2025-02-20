'''Baekjoon 1946 Greedy Algorithm'''
import sys
T = int(input())
while T:
    T -= 1
    N = int(input())
    Candis = [[0, 0] for _ in range(N)]
    for i in range(N):
        Candis[i][0], Candis[i][1] = map(int, sys.stdin.readline().split())
 
    Candis.sort(key=lambda x: x[0])
    Min = Candis[0][1]
    count = 0
    for i in range(len(Candis)):
        if Candis[i][1] > Min:
            count += 1
        elif Candis[i][1] < Min:
            Min = Candis[i][1]

    print(N-count)

