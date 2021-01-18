# https://leetcode.com/problems/longest-string-chain/
import math
import os
import random
import re
import sys

from collections import defaultdict
d = defaultdict(int)
        
def longestChain(words):
    words = list(set(words))
    words = sorted(words, key = lambda x: (len(x), x))
    for i in range(0, len(words)):
        word = words[i]
        d[word] = 1
        for j in range(0, len(word)):
            tmp = word[:j]+word[j+1:]
            if tmp in d.keys():
                d[word] = max(d[word], d[tmp]+1)
    return max(list(d.values()))

if __name__ == '__main__':
