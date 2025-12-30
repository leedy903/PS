import sys
input = sys.stdin.readline

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class Trie():
    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_end = True
    
    def is_prefix(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

N, M = map(int, input().strip().split())

trie = Trie()
for _ in range(N):
    word = input().strip()
    trie.insert(word)

answer = 0
for _ in range(M):
    word = input().strip()
    if trie.is_prefix(word):
        answer += 1

print(answer)