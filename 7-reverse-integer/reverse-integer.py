class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = 1
        if x<0:
            x=x*-1
            sign=-1
        final_num=0
        while x!=0:
            digit=x%10
            final_num=final_num*10+digit
            x=x//10
        final_num*=sign
        if final_num < INT_MIN or final_num > INT_MAX:
            return 0
        return final_num
