from heapq import heappush, heappop
def solution(n, k, enemy):
    answer = len(enemy)
    history = []
    
    for i in range(len(enemy)):
        n -= enemy[i]
        heappush(history, -enemy[i])
        if n < 0:
            if k > 0:
                n += -heappop(history) if history else 0
                k -= 1
            else:
                answer = i
                break
    
    return answer