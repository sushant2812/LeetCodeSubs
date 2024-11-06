class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for idx,temperature in enumerate(temperatures):
            while stack!=[] and temperature>temperatures[stack[-1]]:
                temp_idx = stack.pop()
                res[temp_idx]=(abs(temp_idx-idx))
            stack.append(idx)
        return res