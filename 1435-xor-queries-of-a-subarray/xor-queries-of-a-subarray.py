class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_arr = []
        prefix = 0
        for idx, ele in enumerate(arr):
            prefix = prefix^ele
            prefix_arr.append(prefix)
        ans = []
        for left,right in queries:
            if left==0:
                ans.append(prefix_arr[right])
            else:
                ans.append(prefix_arr[right]^prefix_arr[left-1])
        return ans