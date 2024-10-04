class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        print(skill)      
        strong = skill.pop(len(skill)-1)
        weak = skill.pop(0)
        match = weak+strong
        res = weak*strong
        while skill!=[]:
            strong = skill.pop(len(skill)-1)
            weak = skill.pop(0)
            if strong+weak!=match:
                return -1
            else:
                res += strong*weak
        return res
