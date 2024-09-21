class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        stack = []
        for pos,sped in sorted(pairs)[::-1]:
            stack.append((target-pos)/sped)
            if (len(stack)>= 2 and stack[-1]<=stack[-2]):
                stack.pop()
        return len(stack)