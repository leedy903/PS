import sys
input = sys.stdin.readline

def dfs(depth, expression):
    global zero_list
    if depth == N:
        if eval(expression.replace(" ", "")) == 0:
            zero_list.append(expression)
        return

    for operand in ("+", "-", " "):
        dfs(depth + 1, expression + operand + str(depth + 1))
    

T = int(input())
for test_case in range(T):
    N = int(input())
    zero_list = []
    dfs(1, "1")
    zero_list.sort()
    for expression in zero_list:
        print(expression)
    print()