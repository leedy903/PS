Count = 0
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    Count += 1
    M = L if V%P > L else V%P 
    Ans = (V//P)*L + M
    print("Case {0}: {1}".format(Count, Ans))