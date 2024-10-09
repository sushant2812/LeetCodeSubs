# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if node is None:
                return 0
            left_subtree = dfs(node.left)
            right_subtree = dfs(node.right)
            self.ans = max(self.ans,left_subtree+right_subtree)
            return 1+max(left_subtree,right_subtree)
        dfs(root)
        return self.ans