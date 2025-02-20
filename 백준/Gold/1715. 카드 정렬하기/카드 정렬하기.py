import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    heappush(cards, int(input()))

answer = 0
while len(cards) > 1:
    a = heappop(cards)
    b = heappop(cards)
    compare = a + b
    answer += compare
    heappush(cards, compare)

print(answer)