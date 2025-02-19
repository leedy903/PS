import sys
input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

left, right = 1, max(cables)
while left <= right:
    mid = (left + right) // 2
    count = 0
    for cable in cables:
        count += cable // mid
    if count >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)