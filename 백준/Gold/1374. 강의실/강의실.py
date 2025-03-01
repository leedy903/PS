import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
lectures = [list(map(int, input().rstrip().split())) for _ in range(n)]
lectures.sort(key = lambda x : x[1])

classrooms = [lectures[0][2]]

for lecture in lectures[1:]:
    if classrooms and classrooms[0] <= lecture[1]:
        heappop(classrooms)
    heappush(classrooms, lecture[2])
    
print(len(classrooms))
