def solution(queue1, queue2):
    answer = -2
    
    queue = queue1 + queue2
    queue_sum = sum(queue)
    
    if queue_sum % 2:
        answer = -1
        return answer
    
    goal = queue_sum // 2
    
    start = 0
    end = len(queue1)
    q1_sum = sum(queue1)
    
    time = 0
    while True:
        if start == end or end >= len(queue):
            answer = -1
            break
        
        if q1_sum > goal:
            q1_sum -= queue[start]
            start += 1
            time += 1
        elif q1_sum < goal:
            q1_sum += queue[end]
            end += 1
            time +=1
        else:
            answer = time
            break
        
    return answer