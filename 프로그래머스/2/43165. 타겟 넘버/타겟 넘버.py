def dfs(numbers, depth, total, target):
    ret = 0
    if depth == len(numbers):
        if total == target:
            return 1
        else:
            return 0
        
    ret += dfs(numbers, depth + 1, total + numbers[depth], target)
    ret += dfs(numbers, depth + 1, total - numbers[depth], target)
    
    return ret
    


def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer