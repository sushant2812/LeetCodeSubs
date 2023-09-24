class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n%2==0:
            mid1=nums1[n//2-1]
            mid2=nums1[n//2]
            ans = (mid1+mid2)/2.0
        else:
            ans = nums1[n//2]
        return ans

