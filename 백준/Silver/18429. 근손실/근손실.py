import sys
from itertools import permutations as permu
input = sys.stdin.readline
n, k = map(int, input().split())
kits = list(map(int, input().split()))

count = 0
kits = list(permu(kits))

for kit in kits:
    weight = 500
    for add_weight in kit:
        weight += add_weight - k
        if weight < 500:
            break
    else:
        count += 1
print(count)