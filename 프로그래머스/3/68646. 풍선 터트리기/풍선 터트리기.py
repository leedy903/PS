def solution(a):
    answer = 0
    left_min = [float('inf') for _ in range(len(a))]
    right_min = [float('inf') for _ in range(len(a))]
    
    for i in range(1, len(a)):
        left_min[i] = min(a[i - 1], left_min[i - 1])    
    
    for i in range(len(a) -2, -1, -1):
        right_min[i] = min(a[i + 1], right_min[i + 1])
    
    for i in range(len(a)):
        if left_min[i] < a[i] and right_min[i] < a[i]:
            answer += 1
    answer = len(a) - answer
    return answer