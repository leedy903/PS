M = int(input())
Count = 0
C = 1000-M
Clist = [500, 100, 50, 10, 5, 1]
for Citem in Clist:
    Count += C//Citem
    C %= Citem
print(Count) 
