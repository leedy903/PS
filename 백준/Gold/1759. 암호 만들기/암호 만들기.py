L, C = map(int, input().split())
alphabet = input().split()
alphabet.sort()

vowel = list("aeiou")
consonant = list("bcdfghjklmnpqrstvwxyz")
candidates = []

def dfs(code, index):
    global candidates, L

    if len(code) == L:
        vowel_count = sum([code.count(v) for v in vowel])
        consonant_count = sum([code.count(c) for c in consonant])
        if vowel_count > 0 and consonant_count > 1:
            candidates.append(code)
        return
    
    for i in range(index, len(alphabet)):
        dfs(code + alphabet[i], i + 1)
    
dfs("", 0)
for candidate in candidates:
    print(candidate)