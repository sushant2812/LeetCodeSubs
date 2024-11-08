# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        nodes = []
        if root==None:
            return []
        queue.append(root)
        while queue!=[]:
            subnodes=[]
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                subnodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            nodes.append(subnodes)
        return nodes
