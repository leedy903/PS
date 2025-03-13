def solution(answers):
    answer = []
    supotrio = [0, 0, 0]
    supo1pat = [1, 2, 3, 4, 5]
    supo2pat = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3pat = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    pat1len = len(supo1pat)
    pat2len = len(supo2pat)
    pat3len = len(supo3pat)
    
    for i, ans in enumerate(answers):
        if ans == supo1pat[i%pat1len]:
            supotrio[0] += 1
        if ans == supo2pat[i%pat2len]:
            supotrio[1] += 1
        if ans == supo3pat[i%pat3len]:
            supotrio[2] += 1
    
    max_score = max(supotrio)
    for i in range(len(supotrio)):
        if supotrio[i] == max_score:
            answer.append(i + 1)
            
    return answer