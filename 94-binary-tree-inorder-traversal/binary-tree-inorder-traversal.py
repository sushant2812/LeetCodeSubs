# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        queue=[]
        while queue or root:
            ## Traversing teh left subtree
            while root:
                queue.append(root)
                root=root.left
            root=queue.pop()
            ans.append(root.val)
            root=root.right
        return ans