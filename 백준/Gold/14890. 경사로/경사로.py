import sys

N, L = map(int, sys.stdin.readline().split())
_map = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    _map[i] = list(map(int, sys.stdin.readline().split()))

answer = 0

def get_level_counts(mode) -> list:
    level_counts = []
    for i in range(N):
        level_count = []
        for j in range(N):
            if mode == 'vertical':
                level = _map[j][i]
            elif mode == 'horizontal':
                level = _map[i][j]
            if level_count and level_count[-1][0] == level:
                level_count[-1][1] += 1
            else:
                level_count.append([level, 1])
        level_counts.append(level_count)
    return level_counts
     
def path_count(level_counts) -> int:
    path_count = 0
    for level_count in level_counts:
        is_path = True
        set_slide = False
        for index, (level, count) in enumerate(level_count):
            if index > 0:
                prev_level, prev_count = level_count[index - 1]
                if abs(level - prev_level) > 1:
                    is_path = False
                    break
                if level == prev_level + 1:
                    if set_slide:
                        if prev_count < 2 * L:
                            is_path = False
                            break
                        else:
                            set_slide = False
                    else:
                        if prev_count < L:
                            is_path = False
                            break
                
                if level == prev_level - 1:
                    if count >= L:
                        set_slide = True
                    else:
                        is_path = False
                        break
        if is_path:
            path_count += 1
    return path_count

vertical_level_counts = get_level_counts('vertical')
horizonatal_level_counts = get_level_counts('horizontal')
answer += path_count(vertical_level_counts)
answer += path_count(horizonatal_level_counts)

print(answer)