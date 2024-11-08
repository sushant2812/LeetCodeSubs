# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        def helper(node):
            if not node:
                return 0
            left=node.left
            right=node.right
            return 1+max(helper(node.left),helper(node.right))
        lh=helper(root.left)
        rh=helper(root.right)
        if abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False