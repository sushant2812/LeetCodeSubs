class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        temp_counter = 0
        for right in range(len(s)-1,-1,-1):
            if s[right]=='1':
                ans+=temp_counter
            else:
                temp_counter+=1
        return ans