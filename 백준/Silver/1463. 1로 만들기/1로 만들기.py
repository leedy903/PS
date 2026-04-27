N = int(input())
D = [0]*(N+1)

for i in range(2, N+1):
    D[i] = D[i-1] + 1
    if not i%2:
        D[i] = min(D[i], D[i//2] + 1)
    if not i%3:
        D[i] = min(D[i], D[i//3] + 1)

print(D[N])