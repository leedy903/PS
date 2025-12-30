import sys
input = sys.stdin.readline

class Node():
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class Trie():
    def __init__(self) -> None:
        self.root = Node()
        self.count = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def scan(self):        
        def dfs(node, push, depth):
            for key in node.children.keys():
                child = node.children[key]
                if child.is_end:
                    self.count += push
                next_push = push + 1 if len(child.children.keys()) > 1 or child.is_end else push
                dfs(child, next_push, depth + 1)

        dfs(self.root, 1, 0)

while True:
    trie = Trie()
    line = input().strip()
    if not line:
        break

    N = int(line)

    for _ in range(N):
        word = input().strip()
        trie.insert(word)

    trie.scan()
    print(f"{round(trie.count / N, 2):.2f}")