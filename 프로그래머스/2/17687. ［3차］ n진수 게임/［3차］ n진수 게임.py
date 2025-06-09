def solution(n, t, m, p):
    answer = "0"
    digit = list("0123456789ABCDEF")
    for number in range(1, t * m + 1):
        result = ""
        while number > 0:
            result += digit[number % n]
            number //= n
        answer += result[::-1]
    
    return answer[p - 1::m][:t]