import sys
from functools import cmp_to_key
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def convex_hull(points):
    origin = min(points, key=lambda p: (p[1], p[0]))

    def cmp(p1, p2):
        cross = ccw(origin, p1, p2)
        if cross > 0:
            return -1
        if cross < 0:
            return 1

        dist_p1 = dist(origin, p1)
        dist_p2 = dist(origin, p2)

        if dist_p1 < dist_p2:
            return -1
        if dist_p1 > dist_p2:
            return 1
        return 0
    
    sorted_points = [p for p in points if p != origin]
    sorted_points.sort(key=cmp_to_key(cmp))

    stack = [origin]
    for p in sorted_points:
        while len(stack) >= 2 and ccw(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)
    return stack

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
print(len(convex_hull(points)))