def solution(gems):    
    gem_set = set(gems)
    N = len(gems)
    answer = [0, N - 1]
    gem_collect = {gems[0]:1}
    start, end = 0, 0
    
    while start < N and end < N:
        if len(gem_set) == len(gem_collect):
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                gem_collect[gems[start]] -= 1
                if gem_collect[gems[start]] == 0:
                    del gem_collect[gems[start]]
                start += 1
        else:
            end += 1
            if end == N:
                break
            gem_collect[gems[end]] = gem_collect.get(gems[end], 0) + 1
            
            
    return [answer[0] + 1, answer[1] + 1]