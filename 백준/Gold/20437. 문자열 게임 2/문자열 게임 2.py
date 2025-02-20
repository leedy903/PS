import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    string = list(input().rstrip())
    k = int(input())
    min_len, max_len = len(string), 0

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index_map = {alphabet : [] for alphabet in alphabets}
    
    for i in range(len(string)):
        index_map[string[i]].append(i)

    for alphabet, index_list in index_map.items():
        for i in range(len(index_list) - k + 1):
            min_len = min(min_len, index_list[i + k - 1] - index_list[i] + 1)
            max_len = max(max_len, index_list[i + k - 1] - index_list[i] + 1)

    print(-1 if max_len == 0 else f"{min_len} {max_len}")