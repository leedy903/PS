dices = list(map(int, input().split()))
price = 0
if dices[0] == dices[1] == dices[2]:
    price = 10000 + dices[0] * 1000
elif dices[0] == dices[1] and dices[1] != dices[2]:
    price = 1000 + dices[0] * 100
elif dices[1] == dices[2] and dices[0] != dices[1]:
    price = 1000 + dices[1] * 100
elif dices[0] == dices[2] and dices[1] != dices[2]:
    price = 1000 + dices[2] * 100
else:
    price = max(dices) * 100
print(price)