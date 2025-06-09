def solution(s):
    answer = 0
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i : j]):
                answer = max(answer, j - i)
    
    return answer

def is_palindrome(x):
    return x == x[::-1]