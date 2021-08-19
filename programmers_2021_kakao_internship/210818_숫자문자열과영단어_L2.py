number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def solution(s):
    if s.isdigit():
        return int(s)

    answer = ''
    idx = 0
    tmp = ''
    while idx < len(s):
        if s[idx].isdigit(): # 숫자이면
            answer += s[idx]
            tmp = ''
        else:
            tmp += s[idx]
            if tmp in number.keys():
                answer += str(number[tmp])
                tmp = ''  
        idx += 1
    return int(answer)

def solution2(s):
    answer = s
    for key, value in number.items():
        answer = answer.replace(key, str(value))
    return int(answer)

solution2("one4seveneight")


