n = int(input())
parents = list(map(int, input().split()))
deleteNode = int(input())

def delete(deleteNode):
    parents[deleteNode] = None
    for i in range(n):
        if parents[i] == deleteNode:
            parents[i] = None
            delete(i)

delete(deleteNode)

leaf = 0
for i in range(n):
    if parents[i] != None and i not in parents:
        leaf += 1

print(leaf)