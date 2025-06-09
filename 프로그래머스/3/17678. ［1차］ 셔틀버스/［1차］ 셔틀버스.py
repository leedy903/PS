from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    
    queue = []
    
    for time in timetable:
        hour, minute = time.split(":")
        queue.append(int(hour) * 60 + int(minute))
    
    queue.sort()
    deq = deque(queue)
    
    bus = 9 * 60
    arrive = 0
    for i in range(n):
        for j in range(m):
            if len(deq) > 0 and bus >= deq[0]:
                arrive = deq.popleft() - 1
            else:
                arrive = bus
        bus += t
    answer = str(arrive // 60).zfill(2) + ":" + str(arrive % 60).zfill(2)
    return answer