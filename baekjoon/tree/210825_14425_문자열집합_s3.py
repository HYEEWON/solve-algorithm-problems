import sys

class Node(object):
    def __init__(self, key, end = None):
        self.key = key
        self.end = end
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(self)
    
    def insert(self, word):
        cur = self.head

        for w in word:
            if w not in cur.child:
                cur.child[w] = Node(w)
            cur = cur.child[w]
        cur.end = True

    def search(self, word):
        cur = self.head
        cnt = 0

        for w in word:
            if w in cur.child:
                cur = cur.child[w]
                cnt += 1
                if len(word) == cnt:
                    return True
            else:
                return False

        if cur.end == True:
            return True

N, M = map(int, sys.stdin.readline().strip().split())

trie = Trie()

for n in range(N):
    word = sys.stdin.readline()

    trie.insert(word)

answer = 0
for i in range(M):
    word = sys.stdin.readline()

    if trie.search(word):
        answer += 1

sys.stdout.write(str(answer))