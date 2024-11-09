class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        temp=[]
        res=[]
        candidates.sort()
        def dfs(idx,target):
            if target==0:
                res.append(temp.copy())
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                temp.append(candidates[i])
                dfs(i+1,target-candidates[i])
                temp.pop()
        dfs(0,target)
        return res