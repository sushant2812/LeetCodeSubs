class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs =[[p,s] for p,s in zip(position,speed)]
        stack = []
        for i,j in sorted(pairs)[::-1]:
            stack.append((target-i)/j)
            if(len(stack)>=2 and stack[-1]<=stack[-2]):
                stack.pop()
        return len(stack)