import sys

input = sys.stdin.readline
N, M, L = map(int, input().split())
stations = list(map(int, input().split()))
stations.append(0)
stations.sort(reverse=True)
distances = []

now = L
for station in stations:
    distances.append(now - station - 1)
    now = station

ans = 0

left, right = 1, L - 1
while left <= right:
    mid = (left + right) // 2
    count = 0
    for distance in distances:
        count += distance // mid
    if count <= M:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)