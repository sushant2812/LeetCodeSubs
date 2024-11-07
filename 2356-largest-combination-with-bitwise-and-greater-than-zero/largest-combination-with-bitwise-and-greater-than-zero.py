class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        pos=[0]*24
        for num in candidates:
            for bit in range(24):
                if num & (1<<bit):
                    pos[bit]+=1
        return max(pos)