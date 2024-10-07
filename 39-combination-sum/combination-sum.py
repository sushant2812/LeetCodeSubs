class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def dfs(idx):
            final = sum(temp)
            if target==final:
                res.append(temp.copy())
                return
            if final>target or idx>=len(candidates):
                return
            temp.append(candidates[idx])
            dfs(idx)
            temp.pop()
            dfs(idx+1)
        dfs(0)
        return res