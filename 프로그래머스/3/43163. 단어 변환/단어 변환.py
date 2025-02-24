min_distance = float("inf")
def solution(begin, target, words):
    answer = 0
    
    
    if target not in words:
        return 0
    
    words_hash = {word: [] for word in words}
    visited = {word: False for word in words}
    
    for key_word in words:
        for value_word in words:
            diff = 0
            for kw, vw in zip(key_word, value_word):
                diff += 1 if kw == vw else 0
            if diff == len(key_word) - 1:
                words_hash[key_word].append(value_word)
    
    for value_word in words:
        diff = 0
        for bw, vw in zip(begin, value_word):
            diff += 1 if bw == vw else 0
        if diff == len(begin) - 1:
            visited[value_word] = True
            dfs(1, value_word, target, words_hash, visited)
    
    answer = min_distance
    return answer


def dfs(depth, now, target, words_hash, visited):
    global min_distance
    if now == target:
        min_distance = min(min_distance, depth)
        return
    
    for value_word in words_hash[now]:
        if visited[value_word] == False:
            visited[value_word] = True
            dfs(depth + 1, value_word, target, words_hash, visited)
            visited[value_word] = False