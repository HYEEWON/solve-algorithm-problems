# String

import re

class Solution:
    # 참고
    # https://leetcode.com/problems/valid-number/discuss/173977/Python-with-simple-explanation
    def isNumber(self, s: str) -> bool:
        has_e = has_dot = has_num = False

        for i, ch in enumerate(s):
            if ch in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:  # +, - 앞은 e/E 이어야 함
                    return False
                elif i == len(s) - 1:
                    return False
            elif ch == '.':
                if has_dot or has_e:  # '.'이 2번 이상 또는 e 다음에 소수가 오는 경우
                    return False
                elif not has_num and i == len(s) - 1:
                    return False
                has_dot = True
            elif ch in ['e', 'E']:
                if not has_num or has_e or i == len(s) - 1:
                    return False
                has_e = True
            elif not ch.isdigit():
                return False
            else:
                has_num = True
        return True

    # 참고
    # https://leetcode.com/problems/valid-number/discuss/23739/Easy-Python-Solution-68-ms-beats-100
    def isNumber2(self, s: str) -> bool:
        if s in ["inf", "-inf", "+inf", "Infinity", "-Infinity", "+Infinity"]:
            return False
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True

    # 참고
    # https://leetcode.com/problems/valid-number/discuss/348874/Python-3-Regex-with-example
    def isNumber3(self, s: str) -> bool:
        # ?: 있거나 없거나
        p = re.compile('^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$')
        return p.match(s)