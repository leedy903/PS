def solution(brown, yellow):
    answer = []
    for height in range(3, 2500):
        for width in range(height, 2500):
            if width + height == (brown//2 + 2) and width * height == brown + yellow:
                answer = [width, height]
                break
    return answer