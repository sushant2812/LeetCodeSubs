class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        num_combo={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        temp=[]
        def dfs(idx):
            if idx==len(digits):
                res.append(''.join(temp))
                return
            for char in num_combo[digits[idx]]:
                temp.append(char)
                dfs(idx+1)
                temp.pop()
        dfs(0)
        return res