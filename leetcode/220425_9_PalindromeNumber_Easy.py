# Math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return x == int(str(x)[::-1])

    # 참고
    # https://leetcode.com/problems/palindrome-number/discuss/316164/Python-no-string-involved
    # 1의 자리 수부터 추출해서 10씩 곱하면서 뒤집어진 숫자 계산
    def isPalindrome2(self, x: int) -> bool:
        original = x
        reverse = 0
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x = x // 10
        return original == reverse