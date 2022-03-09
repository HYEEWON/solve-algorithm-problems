# String, Sliding Window, Hash, Table, Two Pointer

# Sliding Window -> 2 pointer: 조건에 맞지 않으면 end pointer 이동, 조건이 맞으면 start pointer 이동

# Hash Table: t_alpha에 알파벳의 개수 저장
# 알파벳이 Sliding Window에 포함되면 -1
# 개수 <= 0이면 Sliding Window는 해당 알파벳을 모두 포함하고 있는 것

from collections import defaultdict
import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_alpha = defaultdict(int) # t 알파벳 개수
        min_length = sys.maxsize
        answer = ""

        for a in t:
            t_alpha[a] += 1

        # 투 포인터: start, i
        start = 0
        cnt = len(t_alpha.keys())

        # 조건이 만족할 때까지 end 포인터 이동
        for i in range(len(s)):
            if s[i] not in t_alpha.keys():
                continue

            t_alpha[s[i]] -= 1
            if t_alpha[s[i]] == 0:
                cnt -= 1

            if cnt == 0: # sliding window가 t의 모든 문자를 포함하는 경우
                # 조건이 만족하는 동안 start 포인터를 뒤로 이동
                while 1 not in t_alpha.values() and start <= i:
                    if min_length > i - start + 1:
                        min_length = i - start + 1
                        answer = s[start:i + 1]

                    if s[start] in t_alpha.keys():
                        t_alpha[s[start]] += 1
                        if t_alpha[s[start]] > 0:
                            cnt += 1
                    start += 1
        return answer
