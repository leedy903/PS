def solution(sizes):
    answer = 0
    max_horizontal = 0
    max_vertical = 0
    for size in sizes:
        w, h = size
        if w < h:
            w, h = h, w
        max_horizontal = max(max_horizontal, w)
        max_vertical = max(max_vertical, h)
    answer = max_horizontal * max_vertical
    return answer