def solution(n, money):
    answer = 0
    
    dp = [0 for _ in range(n + 1)]
    
    for m in money:
        for i in range(1, n + 1):
            if i == m:
                dp[i] += 1
            if i - m > 0:
                dp[i] += dp[i - m]
    
    answer = dp[-1]
    return answer