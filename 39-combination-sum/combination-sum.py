class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        self.sum=0
        def dfs(idx):
            if self.sum==target:
                res.append(temp.copy())
                return
            if self.sum>target or len(candidates)<=idx:
                return
            temp.append(candidates[idx])
            self.sum+=candidates[idx]
            dfs(idx)
            b=temp.pop()
            self.sum-=b
            dfs(idx+1)
        dfs(0)
        return res