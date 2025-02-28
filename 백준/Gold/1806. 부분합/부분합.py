import sys
input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))

answer = float("inf")

partial_sum = 0
start, end = 0, 0
while start <= end:
    if partial_sum >= s:
        answer = min(answer, end - start)
        partial_sum -= sequence[start]
        start += 1
    elif end < n:
        partial_sum += sequence[end]
        end += 1
    else:
        break

if answer == float("inf"):
    answer = 0
    
print(answer)