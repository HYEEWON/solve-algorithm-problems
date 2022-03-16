# String, Stack

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for b in s:
            if b in ['(', '{', '[']:
                st.append(b)
            else:
                if not st:
                    return False
                if (st[-1] == '(' and b == ')') or (st[-1] == '[' and b == ']') or (st[-1] == '{' and b == '}'):
                    st.pop()
                else:
                    return False

        if st:
            return False
        else:
            return True
