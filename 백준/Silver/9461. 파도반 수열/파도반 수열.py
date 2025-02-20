T = int(input())
for _ in range(T) :
    N = int(input())
    Pad = [1,1,1,2,2]
    if N > 5:
        Temp = [0 for _ in range(N-5)]
        Pad = Pad+Temp
    for i in range(5, N):
        Pad[i] = Pad[i-1] + Pad[i-5]
    print(Pad[N-1])