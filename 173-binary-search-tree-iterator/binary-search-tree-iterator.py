# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            self.stack.append(root.val)
            dfs(root.right)
        dfs(root)


    def next(self) -> int:
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        return len(self.stack)>0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()