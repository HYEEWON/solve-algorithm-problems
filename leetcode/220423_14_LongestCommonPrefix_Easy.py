# String

class Solution:
    def longestCommonPrefix(self, strs):
        answer = ''
        strs = sorted(strs, key=lambda x: len(x)) # min(strs,key=len)
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if strs[0][i] != s[i]:
                    return answer
            answer += strs[0][i]
        return answer