# Array, Math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])
        # list[s::n]: s 인덱스부터 n 간격으로 배열 탐색
        # list[::-1]: 리스트를 역순으로 뒤집음
        # *: 가장 바깥의 [], ()를 벗김
        
        return matrix

    # 참고 링크
    # # https://leetcode.com/problems/rotate-image/discuss/1940320/96-Faster-Python-Solution

    # 대각선 기준으로 뒤집고((0, 0)~(n-1, n-1)), 행 단위로 반대로 뒤집기
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()

# 배열 슬라이스 참고
# https://dojang.io/mod/page/view.php?id=2208