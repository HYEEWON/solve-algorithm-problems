# String

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for i in range(1, n):
            if len(s) == 1:
                s = str(len(s)) + s
                continue
            cnt = 0
            tmp = ''
            for idx in range(0, len(s)):
                if idx == 0 or s[idx] == s[idx-1]:
                    cnt += 1
                else:
                    tmp += str(cnt) + s[idx-1]
                    cnt = 1

            tmp += str(cnt) + s[-1]
            s = tmp
        return s