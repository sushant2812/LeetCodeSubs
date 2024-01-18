class Solution:
    def isValid(self, s: str) -> bool:
        brackets = dict(('()', '[]', '{}'))
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            elif len(stack)==0 or i!=brackets[stack.pop()]:
                return False
        return len(stack)==0