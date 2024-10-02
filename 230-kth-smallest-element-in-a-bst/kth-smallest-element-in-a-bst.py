# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0,0]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            counter[0]+=1
            if counter[0]==k:
                counter[1] = node.val
                return
            dfs(node.right)
        dfs(root)
        return counter[1]