class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        ans=[]

        def helper(open1,close1):
            if open1==close1==n:
                ans.append("".join(stack))
                return
            if open1<n:
                stack.append("(")
                helper(open1+1,close1)
                stack.pop()
            if close1<open1:
                stack.append(")")
                helper(open1,close1+1)
                stack.pop()
        helper(0,0)
        return ans