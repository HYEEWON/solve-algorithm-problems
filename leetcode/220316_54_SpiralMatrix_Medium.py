# Simulation

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

class Solution:
    def spiralOrder(self, matrix):
        answer = [matrix[0][0]]
        w_cnt, h_cnt = len(matrix[0])-1, len(matrix)-1 # 가로, 세로 이동 수

        x, y, dir = 0, 0, -1
        start = True
        while len(answer) < len(matrix[0])*len(matrix):
            dir = (dir+1) % 4
            if dir in [0, 2]: # 가로
                for c in range(w_cnt):
                    x, y = x + dx[dir], y + dy[dir]
                    answer.append(matrix[y][x])
                if not start:
                    w_cnt -= 1
                start = False
            elif dir in [1, 3]: # 세로
                for c in range(h_cnt):
                    x, y = x + dx[dir], y + dy[dir]
                    answer.append(matrix[y][x])
                h_cnt -= 1
        return answer


    # 참고할 풀이
    # https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
    
    # 리스트의 첫줄 pop -> 리스트 회전 -> 첫줄 pop -> 반복
    '''
    |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
    |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
    |7 8 9|      |4 7|
    '''