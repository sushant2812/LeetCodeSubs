class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        prefix_sum = 0
        for i in range(1,len(nums)+1):
            prefix_sum=prefix_sum+nums[i-1]
            self.sums.append(prefix_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1]-self.sums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)