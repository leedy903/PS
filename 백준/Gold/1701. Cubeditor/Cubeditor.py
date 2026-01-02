import sys
input = sys.stdin.readline

word = input().strip()

def get_max_dup_len(word):
    max_dup_len = 0
    n = len(word)

    for start in range(len(word)):
        m = n - start
        dup_len = 0
        lps = [0] * m
        j = 0

        for i in range(1, m):
            while j > 0 and word[start + i] != word[start + j]:
                j = lps[j - 1]

            if word[start + i] == word[start + j]:
                j += 1
                lps[i] = j

            dup_len = max(dup_len, lps[i])

        max_dup_len = max(max_dup_len, dup_len)

    return max_dup_len

print(get_max_dup_len(word))