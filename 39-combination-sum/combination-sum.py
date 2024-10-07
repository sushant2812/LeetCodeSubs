class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def dfs(idx):
            total = sum(temp)
            if total == target:
                res.append(temp.copy())
                return
            if total>target:
                return
            if idx>=len(candidates):
                return
            temp.append(candidates[idx])
            dfs(idx)
            temp.pop()
            dfs(idx+1)
        dfs(0)
        return res