class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        temp=[]
        def dfs(idx):
            chk=sum(temp)
            if chk==target:
                res.append(temp.copy())
                return
            if idx>=len(candidates) or chk>target:
                return
            temp.append(candidates[idx])
            dfs(idx)
            temp.pop()
            dfs(idx+1)
        dfs(0)
        return res
