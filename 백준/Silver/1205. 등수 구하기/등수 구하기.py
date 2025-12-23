import sys
input = sys.stdin.readline

def solv():
    N, score, P = map(int, input().split())
    if N <= 0:
        print(1)
        return
    scores = list(map(int, input().split()))

    if N == P and score <= scores[-1]:
        print(-1)
        return
    rank = N + 1
    for i in range(N):
        if scores[i] <= score:
            rank = i + 1
            break
    print(rank)
        
solv()