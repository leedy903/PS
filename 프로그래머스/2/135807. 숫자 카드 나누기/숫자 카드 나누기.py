from math import gcd

def solution(arrayA, arrayB):
    def get_gcd(arr):
        g = arr[0]
        for i in range(1, len(arr)):
            num = arr[i]
            g = gcd(g, num)
        return g
    
    def valid(g, arr):
        for num in arr:
            if num % g == 0:
                return False
        return True
    
    gA = get_gcd(arrayA)
    gB = get_gcd(arrayB)
    
    answer = 0
    if valid(gA, arrayB):
        answer = max(answer, gA)
    if valid(gB, arrayA):
        answer = max(answer, gB)
            
    return answer