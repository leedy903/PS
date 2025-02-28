import sys
input = sys.stdin.readline

def binary_search_lower_bound(ball_sizes, target):
    start = 0
    end = len(ball_sizes)
    while start < end:
        mid = (start + end) // 2
        if target <= ball_sizes[mid]:
            end = mid
        else:
            start = mid + 1
    return start

N = int(input())

balls = []
color_sizes = dict()
color_size_sums = dict()

for i in range(N):
    color, size = map(int, input().split())
    balls.append([color, size])
    if color not in color_sizes:
        color_sizes[color] = []
    color_sizes[color].append(size)

every_sizes = sorted([size for _, size in balls])
every_size_sums = [0 for _ in range(N + 1)]
for i in range(1, len(every_sizes) + 1):
    every_size_sums[i] = every_size_sums[i - 1] + every_sizes[i - 1]

for color in color_sizes.keys():
    color_sizes[color].sort()
    ball_sizes = color_sizes[color]
    color_size_sums[color] = [0 for _ in range(len(ball_sizes) + 1)]
    for i in range(1, len(ball_sizes) + 1):
        ball_size = ball_sizes[i - 1]
        color_size_sums[color][i] = color_size_sums[color][i - 1] + ball_size

for ball in balls:
    color, size = ball
    sum_size = 0
    total_sum_index = binary_search_lower_bound(every_sizes, size)
    sum_size = every_size_sums[total_sum_index]
    same_color_index = binary_search_lower_bound(color_sizes[color], size)
    sum_size -= color_size_sums[color][same_color_index]
    print(sum_size)