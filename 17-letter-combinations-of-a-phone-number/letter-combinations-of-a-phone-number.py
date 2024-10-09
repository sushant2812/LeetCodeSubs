class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        output = []
        combination = []
        phone_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def backtrack(idx):
            if idx==len(digits):
                output.append(''.join(combination))
                return
            for char in phone_map[digits[idx]]:
                combination.append(char)
                backtrack(idx+1)
                combination.pop()
        backtrack(0)
        return output