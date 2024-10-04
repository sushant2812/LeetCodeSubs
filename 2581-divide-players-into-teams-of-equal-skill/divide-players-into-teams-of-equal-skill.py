class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()   
        left = 0
        right = len(skill)-1
        match = skill[left]+skill[right]
        res = skill[left]*skill[right]
        left = left+1
        right = right-1
        while left<right:
            strong = skill[right]
            weak = skill[left]
            if strong+weak!=match:
                return -1
            else:
                res += strong*weak
            left=left+1
            right=right-1
        return res
