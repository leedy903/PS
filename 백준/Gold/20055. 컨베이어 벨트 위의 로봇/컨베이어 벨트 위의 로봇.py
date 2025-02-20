from collections import deque

N, K = map(int, input().split())
Belts = deque(map(int, input().split()))
Robots = deque([False for _ in range(N)])

count = 0
while(Belts.count(0) < K):
    count += 1
    Belts.rotate()
    if Robots[-1]:
        Robots[-1] = False
    Robots.rotate()
    if Robots[-1]:
        Robots[-1] = False
    for i in range(N - 2, -1, -1):
        if Robots[i] and not Robots[i+1] and Belts[i+1] > 0:
            Robots[i] = False
            Robots[i+1] = True
            Belts[i+1] -= 1
    
    if Belts[0] > 0:
        Belts[0] -= 1
        Robots[0] = True
    
print(count)