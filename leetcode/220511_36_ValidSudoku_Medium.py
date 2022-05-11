# Array, Hash Table, Matrix

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 가로
        for y in range(9):
            flag = defaultdict(False)
            for x in range(9):
                if board[y][x] not in flag.keys():
                    flag[board[y][x]] = True
                else:
                    return False
        # 세로
        for x in range(9):
            flag = defaultdict(False)
            for y in range(9):
                if board[y][x] not in flag.keys():
                    flag[board[y][x]] = True
                else:
                    return False
        # 사각형
        s_y, s_x = 0, 0
        for j in range(3):
            for i in range(3):
                flag = defaultdict(False)
                for y in range(s_y, s_y+3):
                    for x in range(s_x, s_x+3):
                        if board[y][x] not in flag.keys():
                            flag[board[y][x]] = True
                        else:
                            return False
                s_x += 3
            s_y += 3
        return True