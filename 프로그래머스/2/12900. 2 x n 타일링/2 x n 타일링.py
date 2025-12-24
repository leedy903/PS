def solution(n):
    a, b = 1, 2
    if n < 3:
        return n
    for i in range(3, n + 1):
        next = (a + b) % 1_000_000_007
        a = b
        b = next
    answer = b
    return answer