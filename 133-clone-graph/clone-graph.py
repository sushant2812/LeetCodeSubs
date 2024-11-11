"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = {}
        visited =set()
        queue= [node]
        while queue:
            temp = queue.pop(0)
            if temp in visited:
                continue
            visited.add(temp)
            nodes[temp.val]=[]
            for i in temp.neighbors:
                nodes[temp.val].append(i.val)
                queue.append(i)
        copied_nodes = {}
        for i in nodes:
            copied_nodes[i]=Node(i)
        for i in nodes:
            copied_nodes[i].neighbors=[]
            for j in nodes[i]:
                copied_nodes[i].neighbors.append(copied_nodes[j])
        return copied_nodes[node.val]