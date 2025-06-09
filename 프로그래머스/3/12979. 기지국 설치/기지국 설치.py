import math
def solution(n, stations, w):
    answer = 0
    left = 1
    cover_area = 2 * w + 1
    for station in stations:
        answer += math.ceil((station - w - left) / cover_area)
        left = station + w + 1

    answer += math.ceil((n - left + 1) / cover_area)
        
    return answer