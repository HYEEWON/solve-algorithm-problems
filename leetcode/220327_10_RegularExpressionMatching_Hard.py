# String, DP

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        reg = re.compile('^' + p + '$')
        return reg.search(s)

    # 참고 풀이
    # https://leetcode.com/problems/regular-expression-matching/discuss/336345/Python-simple-DP
    def isMatch2 (self, s, p):
        # dp[i][j] = p[:i], s[:j]의 매칭 여부
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True

        for i in range(2, len(p)+1): # s는 공백, p는 공백이 아닐 경우
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]


        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in [s[i-1], '.']:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] # '*'의 의미가 zero
                    if p[j-2] in [s[i-1], '.']: # '*'의 의미가 많음
                        dp[i][j] = dp[i][j] or dp[i-1][j]
        return dp[-1][-1]



