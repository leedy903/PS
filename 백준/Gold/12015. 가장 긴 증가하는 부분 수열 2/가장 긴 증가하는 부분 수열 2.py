import sys
input = sys.stdin.readline

def binary_search(target):
    start, end = 0, len(lis)
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

lis = [0]
n = int(input())
sequence = list(map(int, input().split()))

for i in range(n):
    cur = sequence[i]
    if lis[-1] < cur:
        lis.append(cur)
    else:
        lis[binary_search(cur)] = cur

print(len(lis) - 1)