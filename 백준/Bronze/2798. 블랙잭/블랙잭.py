N, M = map(int, input().split())
card = list(map(int, input().split()))

MAX = 0

for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sum_ = card[i] + card[j] + card[k]
            if (M >= sum_ and sum_ > MAX):
                MAX = sum_;

print(MAX)
