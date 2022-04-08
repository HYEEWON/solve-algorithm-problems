# String

# 참고 풀이
# https://leetcode.com/problems/zigzag-conversion/discuss/3744/A-simple-python-solution-97ms-8-lines
# https://leetcode.com/problems/zigzag-conversion/discuss/124059/Thinking-Process-(Java-Python)

class Solution:
    # 내가 푼 풀이
    # 2차원 배열을 만들어 값을 넣어줌
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        strs = [["" for i in range((len(s)//(numRows*2-2))*(numRows-1) + numRows)] for j in range(numRows)]

        x, idx = 0, 0
        while idx < len(s) and x < len(strs[0]):
            for j in range(numRows):
                if idx >= len(s):
                    break
                strs[j][x] = s[idx]
                idx += 1
            x += 1
            y = numRows-1
            for j in range(numRows-2):
                if idx >= len(s):
                    break
                y = (y-1) % numRows
                strs[y][x] = s[idx]
                x += 1
                idx += 1

        answer = ''
        for j in range(len(strs)):
            answer += ''.join(strs[j])
        return answer
