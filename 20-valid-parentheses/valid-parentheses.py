class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={')':'(','}':'{',']':'['}
        hash=set(['(','{','['])
        for i in s:
            if i in hash:
                stack.append(i)
            elif stack and brackets[i]==stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack)==0