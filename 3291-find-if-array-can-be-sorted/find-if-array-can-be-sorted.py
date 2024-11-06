class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        max_number=0
        current_max=0
        prev_bit= 0
        for n in nums:
            curr_bit = n.bit_count()
            if prev_bit!=curr_bit:
                max_number = current_max
                prev_bit = curr_bit
            if n<max_number:
                return False
            current_max = max(current_max,n)
        return True