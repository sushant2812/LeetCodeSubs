class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:  
                return mid
            if nums[mid]>=nums[left]: ##Left Half is Sorted if true
                if nums[left]<=target<=nums[mid]: ##Target lies between center and left
                    right = mid -1
                else:
                    left = mid+1
            else:
                if nums[mid]<= target <=nums[right]: ## Target lies between center and right therefore need to increment the left
                    left= mid+1
                else:
                    right = mid -1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid]>=nums[left]: ##All numbers are sorted between left and mid
                if nums[left]<=target<=nums[mid]: ##IF true then the target is between these two numbers
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid]<=target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1