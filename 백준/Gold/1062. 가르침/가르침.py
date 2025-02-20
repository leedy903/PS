import sys
input = sys.stdin.readline

def dfs(depth, start):
    global answer
    
    if depth == k:
        count = 0
        for word in words:
            for alphabet in word:
                if not alphabets[ord(alphabet) - ord('a')]:
                    break
            else:
                count += 1

        answer = max(answer, count)
        return

    for i in range(start, 26):
        if not alphabets[i]:
            alphabets[i] = True
            dfs(depth + 1, i + 1)
            alphabets[i] = False

n, k = map(int, input().split())
words = list(set(input().rstrip()[4:-4]) for _ in range(n))
default_alphabets = set("antatica")
alphabets = [False for _ in range(26)]

answer = 0
if k == 26:
    answer = n
elif k >= 5:
    for alphabet in default_alphabets:
        alphabets[ord(alphabet) - ord('a')] = True
    dfs(5, 0)

print(answer)