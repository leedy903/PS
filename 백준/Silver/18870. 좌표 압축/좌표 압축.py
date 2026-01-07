import sys
input = sys.stdin.readline

N = int(input())
points = list(map(int, input().strip().split()))
compressed_points = sorted(list(set(points)))
point_hash = {compressed_points[i] : i for i in range(len(compressed_points))}

answer = []
for i in range(N):
    answer.append(point_hash[points[i]])

print(*answer)