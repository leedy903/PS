from collections import deque

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    deq = deque(B)
    
    for a in A:
        while deq:
            b = deq.popleft()
            if a < b:
                answer += 1
                break
    
    
    return answer