def solution(n):
    fibo = [0 for _ in range(n + 1)]
    fibo[1] = 1
    fibo[2] = 1

    for i in range(3, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    
    answer = fibo[n]
    return answer%1234567