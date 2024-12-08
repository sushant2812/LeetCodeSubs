class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brack={')':'(','}':'{',']':'['}
        hash=set(['{','(','['])
        for i in s:
            if i in hash:
                stack.append(i)
            elif stack and brack[i]==stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack)==0