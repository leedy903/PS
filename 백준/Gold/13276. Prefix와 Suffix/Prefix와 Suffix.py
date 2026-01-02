import sys
input = sys.stdin.readline

word = input().strip()
prefix = input().strip()
suffix = input().strip()

def get_lps(word):
    n = len(word)
    lps = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and word[i] != word[j]:
            j = lps[j - 1]
        
        if word[i] == word[j]:
            j += 1
            lps[i] = j

    return lps

def kmp(word, pattern):
    n, m = len(word), len(pattern)
    lps = get_lps(pattern)
    res = []
    j = 0

    if m == 0:
        return list(range(n + 1))

    for i in range(n):
        while j > 0 and word[i] != pattern[j]:
            j = lps[j - 1]
        
        if word[i] == pattern[j]:
            j += 1

            if j == m:
                res.append(i - m + 1)
                j = lps[j - 1]
            
    return res

answer = 0
prefix_len = len(prefix)
suffix_len = len(suffix)

partial_words = set()
prefix_indices = kmp(word, prefix)
suffix_indices = kmp(word, suffix)

for prefix_idx in prefix_indices:
    for suffix_idx in suffix_indices:
        if prefix_idx <= suffix_idx and prefix_idx + prefix_len <= suffix_idx + suffix_len:
            partial_words.add(word[prefix_idx : suffix_idx + suffix_len])

print(len(partial_words))