import sys

class Node(object):
    def __init__(self, key, count=0, end = None):
        self.key = key
        self.end = end
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None) # 빈 노드를 헤드로 함

    def insert(self, word):
        cur = self.head

        for w in word:
            if w not in cur.child:
                cur.child[w] = Node(W)
            cur = cur.child[w]
        cur.end = True
        
    def search(self, word):
        cur = self.head

        for w in word:
            if w in cur.child:
                cur = cur.child[w]
            else:
                return False

        if cur.end == True:
            return True

def getScore(word):
    if len(word) <= 2:
        return 0
    elif len(word) <= 4:
        return 1
    elif len(word) == 5:
        return 2
    elif len(word) == 6:
        return 3
    elif len(word) == 7:
        return 5
    elif len(word) == 8:
        return 11

def backTracking(y, x, cnt, word):
    global answer, longWord
    if cnt >= 2:
        if trie.search(word):
            answer[word] = cnt
            if cnt > len(longWord):
                longWord = word
            elif cnt == len(longWord):
                longWord = min(longWord, word)

    if cnt == 8:
        return 

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<4 and 0<=ny<4 and visit[ny][nx] == 0:
            visit[ny][nx] = 1
            backTracking(ny, nx, cnt+1, word+board[ny][nx])
            visit[ny][nx] = 0

trie = Trie()

W = int(sys.stdin.readline())
for i in range(W):
    word = sys.stdin.readline().strip()
    trie.insert(word)
input()

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

B = int(sys.stdin.readline().strip())
for b in range(B):
    board = []
    for i in range(4):
        board.append(list(sys.stdin.readline().strip()))

    answer = {}
    longWord = ''
    for i in range(4):
        for j in range(4):    
            visit = [[0 for i in range(4)] for j in range(4)]
            visit[i][j] = 1
            backTracking(i, j, 1, board[i][j])
            visit[i][j] = 0

    totalScore = 0
    for key in answer.keys():
        totalScore += getScore(key)

    sys.stdout.write(str(totalScore)+' '+longWord+' '+str(len(answer.keys()))+'\n')
    if (b < B-1):
        input()