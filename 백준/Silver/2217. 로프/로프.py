K = int(input())
Rope = [0 for _ in range(K)]
for i in range(K):
    Rope[i] = int(input())
Rope.sort(reverse=True)

MaxW = 0
for i in range(len(Rope)):
    W = Rope[i] * (i+1)
    if MaxW < W:
        MaxW = W
    
print(MaxW)