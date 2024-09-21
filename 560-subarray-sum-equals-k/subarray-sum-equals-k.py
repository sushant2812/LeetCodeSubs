class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        total = 0
        prefix_count = {0:1}
        for num in nums:
            prefix_sum += num
            if prefix_sum-k in prefix_count:
                total += prefix_count[prefix_sum-k]
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] +=1
            else:
                prefix_count[prefix_sum] = 1
        return total