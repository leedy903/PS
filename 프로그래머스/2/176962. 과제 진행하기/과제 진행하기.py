from collections import deque
def solution(plans):
    answer = []
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        h, m = map(int, start.split(":"))
        minutes = h * 60 + m
        plans[i][1] = minutes
        plans[i][2] = int(playtime)
        
    plans.sort(key = lambda x : x[1])
    tasks = deque(plans)
    waits = []
    
    while tasks:
        if len(tasks) > 1:
            c_name, c_start, c_playtime = tasks[0]
            n_name, n_start, n_playtime = tasks[1]
            end_time = c_start + c_playtime
            if end_time > n_start:
                waits.append([c_name, end_time - n_start])
                tasks.popleft()
            else:
                answer.append(c_name)
                tasks.popleft()
                gap = n_start - end_time
                while waits:
                    if waits[-1][1] <= gap:
                        w_name, w_time = waits.pop()
                        gap -= w_time
                        answer.append(w_name)
                    else:
                        waits[-1][1] -= gap
                        break
        else:
            answer.append(tasks.popleft()[0])
                        
    return answer + [w_name for w_name, w_time in waits[::-1]]