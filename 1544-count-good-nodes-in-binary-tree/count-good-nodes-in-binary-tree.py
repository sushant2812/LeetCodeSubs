# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxValue):
            if node is None:
                return 0
            cnt = 1 if node.val>=maxValue else 0
            maxValue = max(node.val,maxValue)
            cnt+= dfs(node.left,maxValue)
            cnt+= dfs(node.right,maxValue)
            return cnt
        return dfs(root,root.val)