# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        count = 0
        stack=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            count+=1
            if count==k:
                return root.val
            root=root.right
        return -1
            