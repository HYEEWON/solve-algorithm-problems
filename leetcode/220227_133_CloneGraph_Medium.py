# Grraph, BFS/DFS, Hash Table

# 문제를 이해하는 것에 시간이 걸림
# Input, Output 모두 Node


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        new_node = {node.val: Node(node.val, [])}

        dq = deque()
        dq.append(node)

        while dq:
            cur = dq.popleft()
            
            for next in cur.neighbors:
                # 노드가 추가되지 않았다면 추가
                if next.val not in new_node.keys():
                    new_node[next.val] = Node(next.val, [])
                    dq.append(next)

                # 인접 노드 리스트에 추가
                new_node[cur.val].neighbors.append(new_node[next.val])
                
        return new_node[node.val]