import sys
from itertools import combinations as combi
input = sys.stdin.readline

n, m, r = map(int, input().strip().split())
piles = list(map(int, input().strip().split()))
poles = list(map(int, input().strip().split()))

piles.sort()
poles.sort()

pile_combi = list(combi(piles, 2))
bases = set(abs(p1 - p2) for p1, p2 in pile_combi)

max_area = -1

for base in bases:
    start, end = 0, m
    while start < end:
        mid = (start + end) // 2
        if base * poles[mid] <= r * 2 :
            start = mid + 1
        else:
            end = mid
    cur_area = round(base * poles[start - 1] / 2)
    
    if cur_area <= r:
        max_area = max(round(base * poles[start - 1] / 2, 2), max_area)

print(max_area)