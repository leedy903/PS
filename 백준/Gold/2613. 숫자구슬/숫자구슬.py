import sys
input = sys.stdin.readline

N, M = map(int, input().split())
beads = list(map(int, input().split()))

left, right = max(beads), sum(beads)
minimum_max_prefix = right
while left <= right:
    mid = (left + right) // 2
    prefix_sum = 0
    count = 1
    for i in range(N):
        if mid < prefix_sum + beads[i]:
            count += 1
            prefix_sum = beads[i]
        else:
            prefix_sum += beads[i]

    if count <= M:
        minimum_max_prefix = mid
        right = mid - 1
    else:
        left = mid + 1

groups = []
prefix_sum = 0
beads_count = 0
remain_groups = M

for i in range(N):
    if minimum_max_prefix < prefix_sum + beads[i]:
        groups.append(beads_count)
        prefix_sum = beads[i]
        beads_count = 0
        prefix_sum = 0
        remain_groups -= 1
        
    prefix_sum += beads[i]
    beads_count += 1

    if remain_groups > 1 and (N - i) == remain_groups:
        groups.append(beads_count)
        beads_count = 0
        prefix_sum = 0
        remain_groups -= 1

if beads_count > 0:
    groups.append(beads_count)

print(minimum_max_prefix)
print(*groups)