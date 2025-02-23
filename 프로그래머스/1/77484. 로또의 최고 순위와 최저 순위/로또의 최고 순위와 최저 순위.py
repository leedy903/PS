def solution(lottos, win_nums):
    answer = []
    count = 0
    wild_num = 0
    for lotto in lottos:
        if lotto == 0:
            wild_num += 1
        if lotto in win_nums:
            count += 1
    
    best = 7 - (count + wild_num) if (count + wild_num) != 0 else 6
    worst = 7 - count if count != 0 else 6
    answer = [best, worst]
    return answer