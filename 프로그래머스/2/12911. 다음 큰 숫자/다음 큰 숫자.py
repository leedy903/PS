def solution(n):
    answer = 0
    count_one = bin(n).count('1')
    while True:
        n += 1
        if count_one == bin(n).count('1'):
            answer = n
            break
    return answer