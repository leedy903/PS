import sys
input = sys.stdin.readline

def classify(word):
    left, right = 0, len(word) - 1
    while left < right and word[left] == word[right]:
        left += 1
        right -= 1
    
    if right <= left:
        return 0

    if is_palindrome(word[left:right]) or is_palindrome(word[left + 1 : right + 1]):
        return 1
    
    return 2

def is_palindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

T = int(input())
for _ in range(T):
    word = input().strip()
    print(classify(word))