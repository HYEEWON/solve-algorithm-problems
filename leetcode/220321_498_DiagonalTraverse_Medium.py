# Simulation

# 참고
# https://leetcode.com/problems/diagonal-traverse/discuss/1386313/Python-Solution

class Solution:
    def findDiagonalOrder(self, mat):
        answer = []
        width, height = len(mat[0]), len(mat)
        y, x = 0, 0
        while len(answer) < width*height:
            while y>=0 and x<width: # 위
                answer.append(mat[y][x])
                y -= 1
                x += 1
            if x == width: # y== -1인 경우
                y += 2
                x = width-1
            else: # 오른쪽에 내려갈 수 있는 경우가 남아있음
                y = 0
            while y<height and x>=0: # 아래
                answer.append(mat[y][x])
                y += 1
                x -= 1
            if y == height:
                y = height-1
                x += 2
            else: # 아래쪽에 올라갈 수 있는 경우가 남아있음
                x = 0
        return answer


s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))