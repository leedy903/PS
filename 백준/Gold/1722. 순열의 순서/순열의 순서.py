import sys
import math
input = sys.stdin.readline

n = int(input())
cmd = list(map(int, input().rstrip().split()))

def findKth(k):
    sequence = []
    for i in range(n, 0, -1):
        case_size = math.factorial(i - 1)
        index = (k - 1) // case_size
        sequence.append(numbers.pop(index))
        k = (k - 1) % case_size + 1
    return ' '.join(map(str, sequence))
    
    
def findSequenceRank(sequence):
    rank = 1
    for i in range(n, 0, -1):
        case_size = math.factorial(i - 1)
        index = numbers.index(sequence[n - i])
        del numbers[index]
        rank += case_size * index
        
    return rank
        
answer = ""
q_type = cmd[0]
numbers = list(range(1, n + 1))
if q_type == 1:
    k = cmd[1]
    answer = findKth(k)
        
elif q_type == 2:
    sequence = cmd[1:]
    answer = findSequenceRank(sequence)
    
print(answer)