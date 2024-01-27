"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = {None:None}
        cur_node = head
        while cur_node is not None:
            temp[cur_node] = Node(cur_node.val)
            cur_node = cur_node.next
        curr_node = head
        while curr_node:
            node = temp[curr_node]
            node.next = temp[curr_node.next]
            node.random = temp[curr_node.random]
            curr_node = curr_node.next
        return temp[head]
