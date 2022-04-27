# String, DP

class Solution:
    # 참고
    # https://leetcode.com/problems/longest-palindromic-substring/discuss/119765/Python-DP-solution

    def longestPalindrome(self, s: str) -> str:
        # i~j가 Palindrome이면 dp[i][j] = True
        dp = [[False] * len(s) for i in range(len(s))]
        start, end = 0, 0

        # 길이 1
        for i in range(len(s)):
            dp[i][i] = True

        # 길이 2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if not start and not end:
                    start, end = i, i + 1

        # 그 외
        for i in range(2, len(s)):  # 길이
            for j in range(len(s) - 2):  # 시작점
                if i + j == len(s):
                    break

                if dp[j + 1][i + j - 1] and s[j] == s[i + j]:
                    dp[j][i + j] = True

                    if i > end - start:
                        start, end = j, i + j

        return s[start:end + 1]