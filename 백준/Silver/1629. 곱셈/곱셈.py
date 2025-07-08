import sys
input = sys.stdin.readline

a, b, c = map(int, input().strip().split())

result = 1
while b > 0:
    if b % 2 == 1:
        result *= a
        result %= c
    a *= a
    a %= c
    b //= 2
    
print(result)