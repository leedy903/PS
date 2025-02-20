import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
liquid1, liquid2 = 0, n - 1
left, right = 0, n - 1
nearest = float("inf")
while left < right:
    sum = liquids[left] + liquids[right]
    if abs(sum) < nearest:
        nearest = abs(sum)
        liquid1, liquid2 = liquids[left], liquids[right]
    if sum > 0:
        right -= 1
    else:
        left += 1

print(liquid1, liquid2)