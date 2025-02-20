T = int(input())
Buttons = [300, 60, 10]
Count = [0, 0, 0]
for i in range(len(Buttons)):
    Count[i] = T//Buttons[i]
    T %= Buttons[i]
if T:
    print(-1)
else:
    for count in Count:
        print(count, end=" ")