# String, Hash Table, Sorting

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)

        for a in s:
            s_dict[a] += 1

        for a in t:
            s_dict[a] -= 1

        for a in s_dict:
            if s_dict[a] != 0:
                return False
        return True
