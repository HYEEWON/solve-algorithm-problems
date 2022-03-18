# Simulation

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        change = []  # ((y, x), val)

        for y in range(len(board)):
            for x in range(len(board[0])):
                self.set_change(board, y, x, change)

        for c in change:
            board[c[0][0]][c[0][1]] = c[1]


    def set_change(self, board, y, x, change):
        dx = [0, 0, 1, -1, -1, 1, -1, 1]
        dy = [1, -1, 0, 0, -1, -1, 1, 1]
        cnt = {0: 0, 1: 0}

        for i in range(8):
            ny, nx = dy[i] + y, dx[i] + x
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
                cnt[board[ny][nx]] += 1

        if board[y][x] == 1:
            if cnt[1] < 2:
                change.append(((y, x), 0))
            elif cnt[1] > 3:
                change.append(((y, x), 0))
        else:
            if cnt[1] == 3:
                change.append(((y, x), 1))