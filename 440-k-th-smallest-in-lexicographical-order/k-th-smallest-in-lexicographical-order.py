class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps
        
        curr = 1
        k -= 1  # We start from 1, so we reduce k by 1.
        
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # Move to the next sibling in lexicographical order.
                k -= steps
                curr += 1
            else:
                # Go to the next child.
                curr *= 10
                k -= 1
        
        return curr