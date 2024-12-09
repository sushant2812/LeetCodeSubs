class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        temp=[]
        self.sum=0
        def dfs(idx):
            if self.sum==target:
                res.append(temp.copy())
                return
            if idx>=len(candidates) or self.sum>target:
                return
            temp.append(candidates[idx])
            self.sum+=candidates[idx]
            dfs(idx)
            temp.pop()
            self.sum-=candidates[idx]
            dfs(idx+1)
        dfs(0)
        return res