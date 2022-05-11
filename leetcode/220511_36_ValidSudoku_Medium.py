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

    # 참고
    # https://leetcode.com/problems/valid-sudoku/discuss/15509/Clean-and-Easy82ms-Python
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = set()
        for y in range(9):
            for x in range(9):
                if board[y][x] != '.':
                    # x줄에 board[y][x]가 있음, y 컬럼에 board[y][x]가 있음
                    # 각 구역에 board[y][x]가 있음 ex) (0, 0), (0, 1) 등
                    if (x, board[y][x]) in flag or (board[y][x], y) in flag \
                            or (y//3, x//3, board[y][x]) in flag:
                        return False
                    flag.add((x, board[y][x]))
                    flag.add((board[y][x], y))
                    flag.add((y//3, x//3, board[y][x]))

        return True
