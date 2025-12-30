import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_end = True

    def print(self):
        def dfs(node, depth):
            for key in sorted(node.children.keys()):
                print("--" * depth + key)
                child = node.children[key]
                if not child.is_end:
                    dfs(child, depth + 1)
        dfs(self.root, 0)



N = int(input())

trie = Trie()
for _ in range(N):
    K, *data = list(input().strip().split())
    trie.insert(data)
trie.print()