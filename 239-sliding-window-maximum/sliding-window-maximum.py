class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()
        for idx, num in enumerate(nums):
            while window and window[-1]<num:
                window.pop()
            window.append(num)
            if idx>=k and window[0]==nums[idx-k]:
                window.popleft()
            if idx>=k-1:
                res.append(window[0])
        return res