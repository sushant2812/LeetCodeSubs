class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        lst = []
        for idx in range(len(temperatures)):
            temperature = temperatures[idx]
            while lst and temperature>lst[-1][1]:
                i,temp = lst.pop()
                ans[i] = abs(idx-i)
            lst.append([idx,temperature])
        return ans