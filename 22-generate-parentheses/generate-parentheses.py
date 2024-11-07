class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        def helper(left,right):
            if(left==right==n):
                print(stack)
                ans.append(''.join(stack))
                return
            if(left>right):
                stack.append(')')
                helper(left,right+1)
                stack.pop()
            if(left<n):
                stack.append('(')
                helper(left+1,right)
                stack.pop()
        helper(0,0)
        return ans