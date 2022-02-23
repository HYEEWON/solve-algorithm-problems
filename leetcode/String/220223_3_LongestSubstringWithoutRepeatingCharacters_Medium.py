# 투포인터, 해시
# 부분 문자열의 시작 인덱스와 문자의 인덱스를 비교하며 최대 길이 계산

class Solution:
    def lengthOfLongestSubstring(s):
        sub_string = {}
        length, max_length = 0, 0
        start = 0

        for idx, val in enumerate(s):
            if val not in sub_string.keys():
                sub_string[val] = idx
                length += 1
            else:
                if sub_string[val] >= start:
                    start = sub_string[val] + 1
                    sub_string[val] = idx
                    length = idx - start + 1
                else:
                    sub_string[val] = idx
                    length += 1

            max_length = max(max_length, length)

