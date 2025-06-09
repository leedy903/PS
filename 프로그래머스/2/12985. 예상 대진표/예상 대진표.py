def solution(n,a,b):
    answer = 0
    round = 0
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        round += 1
    answer = round
    return answer