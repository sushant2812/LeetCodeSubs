# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,currMax):
            if (node==None):
                return 0
            cnt = 1 if node.val >= currMax else 0
            currMax = max(currMax,node.val)
            cnt += dfs(node.left,currMax)
            cnt += dfs(node.right,currMax)
            return cnt
        return dfs(root,root.val)