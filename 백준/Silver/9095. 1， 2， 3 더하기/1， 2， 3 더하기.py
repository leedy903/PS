DP = [1,2,4]
for i in range(3 , 11):
    DP.append(DP[i-1] + DP[i-2] + DP[i-3])
T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N-1])