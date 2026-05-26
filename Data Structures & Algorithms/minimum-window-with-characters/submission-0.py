from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):
            return ""
        min_length = float("inf")
        left = 0
        start = 0
        need = Counter(t)
        missing = len(t)
        for r in range(len(s)):
            if need[s[r]]>0:
                missing -=1
            need[s[r]] -=1
            while missing == 0:
                window_len = r-left+1
                if window_len<min_length:
                    min_length = window_len
                    start = left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left +=1
        return "" if min_length == float("inf") else s[start:start + min_length]