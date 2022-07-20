# Trie

def make_trie(root, words):
    for word in words:
        tmp = root
        for w in word:
            tmp.setdefault(w, [0, {}])
            tmp[w][0] += 1
            tmp = tmp[w][1]
    return root

def solution(words):
    answer = 0
    trie = make_trie({}, words)

    for word in words:
        cur = trie
        for i, w in enumerate(word):
            if cur[w][0] > 1:
                cur = cur[w][1]
            else:
                break
        answer += (i+1)
    return answer