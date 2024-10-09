class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        error=0
        open_brackets = 0
        for i in s:
            if i == '(':
                open_brackets += 1
            else:
                if open_brackets>0:
                    open_brackets -=1
                else:
                    error +=1
        return error+open_brackets