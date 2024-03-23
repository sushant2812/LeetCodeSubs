# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,val_to_compare):
        if(root==None):
            return 0
        if(root.val>=val_to_compare):
            self.cnt[0]=self.cnt[0]+1
        self.helper(root.left,max(val_to_compare,root.val))
        self.helper(root.right,max(val_to_compare,root.val))

    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = [0]
        self.helper(root,float('-inf'))
        return self.cnt[0]