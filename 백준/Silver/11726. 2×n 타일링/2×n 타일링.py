N = int(input())
D = [1]*(N+2)
for i in range(2, N+2):
    D[i] = D[i-1] + D[i-2]

print(D[N]%10007)