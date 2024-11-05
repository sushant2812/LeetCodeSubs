class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1  # Search in the left half
                else:
                    left = mid + 1  # Search in the right half
            else:  # Right side is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1  # Search in the right half
                else:
                    right = mid - 1  # Search in the left half
        return -1