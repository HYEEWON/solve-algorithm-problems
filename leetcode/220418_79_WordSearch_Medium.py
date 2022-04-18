# Array, Backtracking, Matrix

class Solution:
    def __init__(self):
        self.visit = []
        self.dy = [-1, 1, 0, 0]
        self.dx = [0, 0, 1, -1]
        self.answer = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    self.visit = [[False for i in range(len(board[0]))] for j in range(len(board))]
                    self.visit[y][x] = True
                    self.dfs(y, x, 1, board, word)
        return self.answer

    def dfs(self, y, x, idx, board, word):
        if idx == len(word):
            self.answer = True
            return

        for i in range(4):
            nx, ny = x + self.dx[i], y + self.dy[i]

            if not 0<=nx<len(board[0]) or not 0<=ny<len(board):
                continue
            if not self.visit[ny][nx] and board[ny][nx] == word[idx]:
                self.visit[ny][nx] = True
                self.dfs(ny, nx, idx+1, board, word)
                self.visit[ny][nx] = False