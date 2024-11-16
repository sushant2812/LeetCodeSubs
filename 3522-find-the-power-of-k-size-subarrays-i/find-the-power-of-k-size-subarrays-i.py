class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        def chk(arr):
            if len(set(arr))==k and arr==sorted(arr) and max(arr)-min(arr)==k-1:
                res.append(max(arr))
            else:
                res.append(-1)
        wind = []
        for i in range(k):
            wind.append(nums[i])
        print(wind)
        chk(wind)
        for j in range(k,len(nums)):
            wind.remove(nums[j-k])
            wind.append(nums[j])
            chk(wind)
        return res