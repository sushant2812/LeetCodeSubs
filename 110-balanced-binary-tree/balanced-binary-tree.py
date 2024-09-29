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
        def helper(root):
            if root==None:
                return 0
            return 1 + max(helper(root.left),helper(root.right))
        lh=helper(root.left)
        rh=helper(root.right)
        if(abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)):
            return True
        return False