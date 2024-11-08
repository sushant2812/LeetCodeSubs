# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        def dfs(node,maxValue):
            if not node:
                return 
            self.cnt+=1 if node.val>=maxValue else 0
            maxValue = max(maxValue,node.val)
            dfs(node.left,maxValue)
            dfs(node.right,maxValue)
        dfs(root,root.val)
        return self.cnt