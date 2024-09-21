class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for idx,temperature in enumerate(temperatures):
            while stack!=[] and stack[-1][-1]<temperature:
                temp_idx, temp_temp = stack.pop()
                ans[temp_idx] = abs(temp_idx-idx)
            stack.append([idx,temperature])
        return ans