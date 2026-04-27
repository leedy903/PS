import sys
input = sys.stdin.readline

n = int(input())
sheets = list(map(int, input().split()))
q = int(input())
questions = [list(map(int, input().split())) for _ in range(q)]
mistakes = [0 for _ in range(n)]
mistake_sums = [0 for _ in range(n)]
answers = []
for i in range(n - 1):
    if sheets[i] > sheets[i + 1]:
        mistakes[i] = 1

mistake_sums[0] = mistakes[0]
for i in range(1, n):
    mistake_sums[i] = mistake_sums[i - 1] + mistakes[i - 1]

for start, end in questions:
    answers.append(mistake_sums[end - 1] - mistake_sums[start - 1])

for answer in answers:
    print(answer)