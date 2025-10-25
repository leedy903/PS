import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    gen = i + sum(list(map(int, str(i))))
    if gen == n:
        print(i)
        break
else:
    print(0)