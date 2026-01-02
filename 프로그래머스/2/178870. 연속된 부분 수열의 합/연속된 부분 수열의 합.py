def solution(sequence, k):
    
    n = len(sequence)
    answer = [0, n - 1]
    start = 0
    prefix_sum = 0
    for end in range(n):
        prefix_sum += sequence[end]
        while k < prefix_sum:
            prefix_sum -= sequence[start]
            start += 1
        if k == prefix_sum and end - start < answer[1] - answer[0]:
            answer = [start, end]
    return answer