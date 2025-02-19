N, K = map(int, input().split())
coin = [0 for i in range(N)]
for i in range(0, N):
    coin[i] = int(input())
count = 0
while(coin):
    if(K >= coin[-1]):
        q, K = divmod(K, coin[-1])
        count += q
    coin.pop()
print(count)

