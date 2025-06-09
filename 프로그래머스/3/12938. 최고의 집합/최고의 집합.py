def solution(n, s):
    share = s // n
    if share == 0:
        answer = [-1]
    else:
        answer = [share for _ in range(n)]
        remain = s % n
        for i in range(1, remain + 1):
            answer[-i] += 1

    return answer