def solution(number, k):
    stack = []
    
    for n in number:
        while len(stack) != 0 and stack[-1] < n and 0 < k:
            stack.pop()
            k -= 1
        
        stack.append(n)
        
    number = ''.join(stack[:len(number) - k])
    return number