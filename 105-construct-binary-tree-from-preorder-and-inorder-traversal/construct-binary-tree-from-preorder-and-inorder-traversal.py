# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        middle = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:middle+1], inorder[:middle+1])
        root.right = self.buildTree(preorder[middle+1:], inorder[middle+1:])
        return root