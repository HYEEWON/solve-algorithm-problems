#(*) 참고한 풀이
def solution(number, k):
    st = []
    for i, n in enumerate(number): 
        while len(st) > 0 and st[-1] < n and k > 0:
            st.pop()
            k -= 1
        if k == 0:
            st += list(number[i:]) # k == 0이면 나머지 숫자를 모두 더함
            break
        st.append(n)
    st = st[:-k] if k > 0 else st # k>0이면 스택 뒤의 k개 숫자를 제거
    answer = ''.join(st)
    return answer

print(solution("4177252841", 4))

# 시간 초과
'''
def solution(number, k):
    answer = ''
    index = -1
    for i in range(len(number)-k): 
        maxN = 0
        for j in range(index+1, k+i+1):
            if maxN < int(number[j]):
                index = j
                maxN = int(number[j])
        answer += str(maxN)
    return answer
'''

# 예제는 맞았으나 채점은 1개를 제외하고 모두 틀림
'''
def solution(number, k):
    cnt, idx = 0, 0
    while (cnt < k and len(number) > 1):
        print(cnt, idx, number)
        if number[idx] < number[idx+1]:
            number = number[:idx]+number[idx+1:]
            cnt += 1
        else:
            idx += 1
        if idx == len(number)-1:
            idx = 0

    return number

print(solution("4177252841", 4))
'''