import sys
from collections import defaultdict

K = int(sys.stdin.readline())
building = list(map(int, sys.stdin.readline().strip().split()))

tree = defaultdict(list)

def dv(level, start, end):
    mid = (start + end) // 2
    node = building[mid]
    tree[level].append(str(node))

    if (start == end):
        return

    dv(level+1, start, mid-1)
    dv(level+1, mid+1, end)


dv(1, 0, len(building)-1)

for key in tree.keys():
    sys.stdout.write(" ".join(tree[key]) + "\n")