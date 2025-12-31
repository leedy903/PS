import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()
answer = 0
start = 0
while start < M:
    if S[start] == 'I':
        end = start + 1
        while True:
            if M <= end or S[end:end + 2] != 'OI':
                break
            end += 2
        if 2 * N + 1 <= end - start:
            answer += 1 + (end - start - (2 * N + 1)) // 2
        
        start = end
    else:
        start += 1
print(answer)