from collections import defaultdict, deque
from itertools import combinations
import sys

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

tree = defaultdict(list)
#line = []
line_num = defaultdict(int)

def bfs_cnt(n, num, visit, combination):
    cut_line = tuple()
    for c in combination:
        cut_line += line_num[c]

    q = deque()
    q.append(n)
    visit[n] = 1

    sum = num[n]
    while q:
        n = q.popleft()
        for node in tree[n]:
            if (node, n) in cut_line or (n, node) in cut_line:
                continue
            if (visit[node] == 0 and node != -1):
                visit[node] = 1
                sum += num[node]
                q.append(node)           
    return sum

def solution(k, num, links):
    answer = sys.maxsize
    n = 0
    check_root = [False for i in range(len(num))]
    for i in range(len(links)):
        #tree[i].append(Node(links[i][0], links[i][1]))
        if links[i][0] != -1:
            tree[i].append(links[i][0])
            tree[links[i][0]].append(i)
            line_num[n] = ((i, links[i][0]), (links[i][0], i))
            n += 1
        if links[i][1] != -1:
            tree[i].append(links[i][1])
            tree[links[i][1]].append(i)
            line_num[n] = ((i, links[i][1]), (links[i][1], i))
            n += 1
    #line = [1 for i in range(n)]

    #print(tree)
    #print(line_num)
    #print(line)
    
    
    for c in combinations([i for i in range(n)], k-1):
        max_cnt = 0
        visit = [0 for i in range(len(num))]
        for  i in range(n):
            if visit[i] == 0:
                #print(c, i, " #############################")
                tmp_cnt = bfs_cnt(i, num, visit, c)
                if tmp_cnt > max_cnt:
                    max_cnt = tmp_cnt
                    #print(tmp_cnt)
        #print(c, max_cnt)    
        if (max_cnt < answer):
            answer = max_cnt

    return answer

#print(solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))
print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
#print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
#print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))