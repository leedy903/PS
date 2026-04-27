import sys

word = input()
pattern = input()

def get_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def kmp(word, pattern):
    lps = get_lps(pattern)
    res = []
    j = 0
    for i in range(len(word)):
        while j > 0 and word[i] != pattern[j]:
            j = lps[j - 1]
        if word[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            res.append(i - len(pattern) + 2)
            j = lps[j - 1]
    return res

searched = kmp(word, pattern)
print(len(searched))
print(*searched)