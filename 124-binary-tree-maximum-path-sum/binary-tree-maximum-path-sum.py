# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def dfs(node):
            if node is None:
                return 0
            left_subtree = max(dfs(node.left),0)
            right_subtree = max(dfs(node.right),0)
            current_sum = left_subtree+right_subtree+node.val
            self.max_sum = max(self.max_sum,current_sum)
            return node.val+max(left_subtree,right_subtree)
        dfs(root)
        return self.max_sum