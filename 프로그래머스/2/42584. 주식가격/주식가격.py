def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i in range(len(prices)):
        while len(stack) > 0 and stack[-1][1] > prices[i]:
            idx, stock = stack.pop()
            answer[idx] = i - idx
        stack.append([i, prices[i]])
    
    while len(stack) > 0:
        idx, stock = stack.pop()
        answer[idx] = len(prices) - idx - 1
    
    return answer