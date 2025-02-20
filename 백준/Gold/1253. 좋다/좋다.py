import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0
for i in range(n):
    target = numbers[i]
    start, end = 0, n - 1
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        now = numbers[start] + numbers[end]
        if now == target:
            count += 1     
            break       
        elif now < target:
            start += 1
        else:
            end -= 1
print(count)