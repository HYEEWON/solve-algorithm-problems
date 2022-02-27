# Bit Manipulation

class Solution:
    # 자바, CPP 등에서는 되지만 파이썬에서는 시간 초과
    def getSum(self, a: int, b: int) -> int:
        if a == 0:
            return b
        if b == 0:
            return a

        while b!=0:
            carry = a&b
            a = a^b
            b = carry << 1

        return a

