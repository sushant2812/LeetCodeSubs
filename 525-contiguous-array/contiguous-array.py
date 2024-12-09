class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Dictionary to store the first occurrence of each cumulative sum (sum_val)
        mp = {}
        # Initialize the cumulative sum
        sum_val = 0
        # Variable to keep track of the maximum length of a balanced subarray
        max_len = 0
        
        # Iterate through the array with indices and values
        for i, num in enumerate(nums):
            # Update the cumulative sum: +1 for 1, -1 for 0
            sum_val += 1 if num == 1 else -1
            
            # Case 1: The entire array from index 0 to i is balanced
            if sum_val == 0:
                # Update max_len to the length of this subarray
                max_len = i + 1
            
            # Case 2: The same sum_val has been seen before
            elif sum_val in mp:
                # Calculate the length of the subarray between the previous index and the current index
                max_len = max(max_len, i - mp[sum_val])
            
            # Case 3: First occurrence of this sum_val
            else:
                # Record the index of the first occurrence of this sum_val
                mp[sum_val] = i
        
        # Return the maximum length of any balanced subarray found
        return max_len
