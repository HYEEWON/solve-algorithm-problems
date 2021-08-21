import re

def solution(new_id):
    answer = ''
    answer = new_id.lower()

    chars = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '\'', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']
    for c in chars:
        answer = answer.replace(c, '')

    while ".." in answer:
        answer = answer.replace("..", ".")

    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:len(answer)-1]
    if answer == '':
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    return answer

def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))