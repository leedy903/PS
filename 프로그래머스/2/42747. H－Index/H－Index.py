def solution(citations):
    answer = 0
    citations.sort()
    N = len(citations)
    for i in range(N):
        if N - i <= citations[i]:
            answer += 1
    return answer