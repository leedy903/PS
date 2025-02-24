def solution(n, times):
    answer = 0
    times.sort()
    
    left, right = 1, times[-1] * n
    
    while left <= right:
        mid = (left + right) // 2
        customer = 0
        for time in times:
            customer += mid // time
            if customer > n:
                break
        
        if customer >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer
    