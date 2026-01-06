from math import factorial
def solution(n, k):
    answer = []
    
    numbers = list(range(1, n + 1))
    
    for i in range(n, 0, -1):
        size = factorial(i - 1)
        index = (k - 1) // size
        answer.append(numbers.pop(index))
        k = (k - 1) % size + 1
    
    return answer