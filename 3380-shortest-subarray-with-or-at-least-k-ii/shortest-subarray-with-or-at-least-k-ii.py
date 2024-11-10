class Solution:  
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def unpackbits(num):
            while num > 0:
                yield num % 2
                num //= 2

        ans, bitwise_or, left, cnt = inf, 0, 0, [0]*32
        for right, num in enumerate(nums):
            bitwise_or |= num
            for i, bit in enumerate(unpackbits(num)):
                cnt[i] += bit
            while bitwise_or >= k and left <= right:
                ans = min(right - left + 1, ans)
                for i, bit in enumerate(unpackbits(nums[left])):
                    cnt[i] -= bit
                    if bit and not cnt[i]:
                        bitwise_or ^= 1 << i
                left += 1
        return -1 if ans == inf else ans