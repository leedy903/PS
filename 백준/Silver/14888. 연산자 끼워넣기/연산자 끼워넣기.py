N = int(input())
operands = list(map(int, input().split()))
operators = list(map(int, input().split()))

MIN, MAX = float('inf'), -float('inf')

def dfs(depth, result, operators):
    global MIN, MAX, operands
    if sum(operators) == 0:
        MIN = min(MIN, result)
        MAX = max(MAX, result)
        return
    
    next_result = 0
    for i in range(4):
        if operators[i] > 0:
            if i == 0:
                next_result = result + operands[depth]
            elif i == 1:
                next_result = result - operands[depth]
            elif i == 2:
                next_result = result * operands[depth]
            else:
                if result < 0:
                    next_result = -result
                    next_result = next_result // operands[depth]
                    next_result = -next_result
                else:
                    next_result = result // operands[depth]

            next_operators = operators[:]
            next_operators[i] -= 1
            dfs(depth + 1, next_result, next_operators)

dfs(1, operands[0], operators)

print(f'{MAX}\n{MIN}')