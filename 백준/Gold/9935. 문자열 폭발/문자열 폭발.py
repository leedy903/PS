words = input()
expolsion_code = input()

stack = []
for w in words:
    stack.append(w)
    if stack[-1] == expolsion_code[-1] and len(stack) >= len(expolsion_code) and ''.join(stack[-len(expolsion_code):]) == expolsion_code:
        for _ in range(len(expolsion_code)):
            stack.pop()

if len(stack) == 0:
    stack = 'FRULA'
print(''.join(stack))