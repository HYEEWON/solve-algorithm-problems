# String, Sliding Window, Hash Table

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_alpha = defaultdict(int)
        answer = 0
        start = 0
        for end in range(len(s)):
            count_alpha[s[end]] += 1

            if (end-start+1)-max(count_alpha.values()) <= k:
                answer = max(answer, end-start+1)
            else:
                count_alpha[s[start]] -= 1
                start += 1

        return answer