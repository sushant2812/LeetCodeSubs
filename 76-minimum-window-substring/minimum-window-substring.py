from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        left = 0
        counter_t = Counter(t)
        counter_temp = {}
        required_chars = len(counter_t)
        formed_chars = 0
        for i in t:
            counter_temp[i]=0

        min_len = float('inf')
        min_window = (0,0)

        for right in range(len(s)):

            if s[right] in counter_t:
                counter_temp[s[right]] +=1
                if counter_t[s[right]] == counter_temp[s[right]]:
                    formed_chars +=1
            while formed_chars == required_chars:
                window_len = right-left+1
                if window_len<min_len:
                    min_len = window_len
                    min_window = (left,right)
                if s[left] in counter_t:
                    counter_temp[s[left]] -= 1
                    if counter_temp[s[left]] < counter_t[s[left]]:
                        formed_chars -=1
                left+=1

        if min_len == float('inf'):
            return ""  
        else:
            return s[min_window[0]:min_window[1] + 1]