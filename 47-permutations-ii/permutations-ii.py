class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        counter = collections.Counter(nums)
        def dfs(temp):
            if len(nums)==len(temp):
                res.append(temp.copy())
                return
            for key in counter.keys():
                if counter[key]==0:
                    continue
                counter[key]-=1
                dfs(temp+[key])
                counter[key]+=1
        dfs([])
        return res