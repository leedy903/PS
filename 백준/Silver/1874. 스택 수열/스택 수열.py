n = int(input())
numbers = [int(input()) for _ in range(n)]
stack = []
top = 1
answer = []
for number in numbers:
    while top <= number:
        stack.append(top)
        answer.append("+")
        top += 1

    if stack[-1] == number:
        stack.pop()
        answer.append("-")
    else:
        answer = ["NO"]
        break

for a in answer:
    print(a)