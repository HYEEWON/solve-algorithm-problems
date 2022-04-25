class Solution:
    def __init__(self):
        self.numbers = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
                        5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
                        8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']
                        }
        self.length = 0
        self.answer = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return self.answer

        digits = list(map(int, digits))
        self.length = len(digits)
        self.backTracking(0, '', digits)

        return self.answer

    def backTracking(self, idx, s, digits):
        if idx >= self.length:
            self.answer.append(s)
            return

        for ch in self.numbers[digits[idx]]:
            s += ch
            self.backTracking(idx + 1, s, digits)
            s = s[:-1]