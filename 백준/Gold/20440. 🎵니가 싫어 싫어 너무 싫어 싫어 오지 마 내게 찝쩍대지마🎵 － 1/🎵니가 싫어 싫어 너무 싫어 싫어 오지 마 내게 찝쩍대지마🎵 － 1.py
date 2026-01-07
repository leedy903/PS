import sys
input = sys.stdin.readline

N = int(input().strip())
points = []
compressed_point = set()
point_hash = dict()

for i in range(N):
    tem, txm = map(int, input().strip().split())
    points.append((tem, txm))
    compressed_point.add(tem)
    compressed_point.add(txm)

compressed_point = sorted(list(compressed_point))
point_hash = {compressed_point[i] : i for i in range(len(compressed_point))}
timeline = [0 for _ in range(len(compressed_point))]

for i in range(N):
    tem, txm = points[i]
    timeline[point_hash[tem]] += 1
    timeline[point_hash[txm]] -= 1

cur = 0
start, end = 0, 0
max_cnt = 0
is_continue = False

for i in range(len(timeline) - 1):
    cur += timeline[i]
    if max_cnt < cur:
        max_cnt = cur
        start = compressed_point[i]
        end = compressed_point[i + 1]
        is_continue = True
    elif max_cnt == cur and is_continue:
        end = compressed_point[i + 1]
    else:
        is_continue = False

print(max_cnt)
print(start, end)
