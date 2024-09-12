class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets = {'}':'{', ')':'(',']':'['}
        for i in s:
            if i in '({[': ###  Appending opening brackets
                stack.append(i)
            elif stack and i in brackets and brackets[i]==stack[-1]:
                stack.pop()
            else:
                return False
        return stack==[]