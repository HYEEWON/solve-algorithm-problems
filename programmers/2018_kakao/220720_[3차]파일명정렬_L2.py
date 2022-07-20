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