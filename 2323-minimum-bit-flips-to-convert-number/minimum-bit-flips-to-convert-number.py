class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        number = start^goal
        number = format(number,'b')
        return number.count('1')