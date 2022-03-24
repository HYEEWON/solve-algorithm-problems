# Simulation

class Solution:
    def fullJustify(self, words, maxWidth):
        answer = []
        cnt, tmp = 0, [] # 단어 길이 합, 단어 배열
        for word in words:
            if cnt + len(word) + len(tmp) <= maxWidth: # 단어 사이의 공백 필수
                cnt += len(word)
                tmp.append(word)
                continue

            if len(tmp) == 1:
                answer.append(tmp[0]+(' '*(maxWidth-len(tmp[0]))))
            else:
                space = [(maxWidth - cnt) // (len(tmp) - 1) for i in range(len(tmp)-1)] # 공백 개수
                for i in range((maxWidth-cnt) % len(space)):
                    space[i] += 1 # 왼쪽부터 공백 개수 증가
                a = ''
                for i in range(len(space)):
                    a += tmp[i] + space[i]*' '
                a += tmp[-1]
                answer.append(a)
            cnt, tmp = len(word), [word]
        answer.append(' '.join(tmp) + ' '*(maxWidth-cnt-len(tmp)+1)) # 마지막은 왼쪽 정렬
        return answer



s = Solution()
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))