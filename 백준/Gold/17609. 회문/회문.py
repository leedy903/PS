import sys
input = sys.stdin.readline

def classify(word):
    left, right = palindrom(word, 0, len(word) - 1)
    if right <= left:
        return 0
    
    semi_left, semi_right = palindrom(word, left + 1, right)
    if semi_right <= semi_left:
        return 1
    
    semi_left, semi_right = palindrom(word, left, right - 1)
    if semi_right <= semi_left:
        return 1
    
    return 2

def palindrom(word, left, right):
    while left < right and word[left] == word[right]:
        left += 1
        right -= 1
    return left, right

T = int(input())
for _ in range(T):
    word = input().strip()
    print(classify(word))