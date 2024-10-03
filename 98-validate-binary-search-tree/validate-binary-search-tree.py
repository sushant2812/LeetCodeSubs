# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower,upper,node):
            if node==None:
                return True
            if(lower<node.val<upper):
                left_subtree = dfs(lower,node.val,node.left)
                right_subtree = dfs(node.val,upper,node.right)
                return left_subtree and right_subtree
            return False
        return dfs(float('-inf'),float('inf'),root)