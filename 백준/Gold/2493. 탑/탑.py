import sys

input = sys.stdin.readline

N = map(int, input())
towers = [0] + list(map(int, input().split()))
answer = []
stack = [0]
for i in range(1, len(towers)):
    while len(stack) > 0 and towers[stack[-1]] < towers[i]:
        stack.pop()
    if len(stack) == 0:
        stack = [0]
    
    answer.append(stack[-1])
    stack.append(i)
    
for a in answer:
    print(a, end = " ")