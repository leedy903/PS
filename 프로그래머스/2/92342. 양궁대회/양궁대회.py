biggest_difference = 0
best_arrows = [0] * 11
apeach_arrows = []
max_arrow_num = 0

def get_score(ryan_arrows: list, apeach_arrows: list) -> tuple:
    ryan_score = 0
    apeach_score = 0
    for i in range(11):
        ryan_arrow, apeach_arrow = ryan_arrows[i], apeach_arrows[i]
        if ryan_arrow == 0 and apeach_arrow == 0:
            continue
        if ryan_arrow > apeach_arrow:
            ryan_score += 10 - i
        else:
            apeach_score += 10 - i
    return ryan_score, apeach_score
            
    
def dfs(depth: int, index: int, ryan_arrows: list) -> None:
    global max_arrow_num, best_arrows, biggest_difference, apeach_arrows
    if depth == 0:
        ryan_score, apeach_score = get_score(ryan_arrows, apeach_arrows)
        if ryan_score > apeach_score:
            score_difference = ryan_score - apeach_score
            if score_difference == biggest_difference:
                for i in range(10, -1, -1):
                    ryan_arrow, best_arrow = ryan_arrows[i], best_arrows[i]
                    if best_arrow > ryan_arrow:
                        return
                    if ryan_arrow > best_arrow:
                        best_arrows = ryan_arrows[:]
                        return
            elif score_difference > biggest_difference:
                biggest_difference = score_difference
                best_arrows = ryan_arrows[:]
    if index < 11:
        apeach_arrow =  apeach_arrows[index]
        next_ryan_arrows = ryan_arrows[:]
        ryan_arrow = apeach_arrow + 1
        if ryan_arrow <= depth:
            next_ryan_arrows[index] = ryan_arrow
            dfs(depth - ryan_arrow, index + 1, next_ryan_arrows)
        next_ryan_arrows[index] = 0
        dfs(depth, index + 1, next_ryan_arrows)
        if index == 9:
            next_ryan_arrows[-1] = depth
            dfs(0, index + 1, next_ryan_arrows)
            
            
def solution(n, info):
    global apeach_arrows, best_arrows, biggest_difference, max_arrow_num
    answer = []
    max_arrow_num = n
    ryan_arrows = [0] * 11
    apeach_arrows = info[:]
    dfs(n, 0, ryan_arrows)
    if biggest_difference == 0:
        answer = [-1]
    else:
        answer = best_arrows[:]
    return answer