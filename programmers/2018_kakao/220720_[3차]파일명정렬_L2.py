# String, Regex

import re

def solution(files):
    # p = re.compile('([A-Z\s\.-]+)([\d]+)([A-Z\s\.-]*)') # 가능
    p = re.compile('([\D]+)([\d]+)(.*)')
    new_files = []
    for i, file in enumerate(files):
        tmp = list(p.findall(file.upper())[0])
        tmp.append(i)
        new_files.append(tmp)
    new_files.sort(key=lambda x: (x[0], int(x[1])))

    answer = []
    for i, new_file in enumerate(new_files):
        answer.append(files[new_file[-1]])
    return answer


def solution2(files):
    p = re.compile('([\D]+)([\d]+)(.*)')
    new_files = []
    for i, file in enumerate(files):
        tmp = list(p.findall(file)[0])
        new_files.append(tmp)
    new_files.sort(key=lambda x: (x[0].lower(), int(x[1])))

    return [''.join(s) for s in new_files]