# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0,0]

        def helper(node):
            if not node:
                return 
            helper(node.left)
            count[0]+=1
            if count[0]==k:
                count[1]=node.val
                return
            helper(node.right)
        helper(root)
        return count[1]