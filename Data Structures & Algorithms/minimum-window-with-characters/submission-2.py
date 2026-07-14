class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        countT, window = {},{}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        Have, Need = 0, len(countT)
        res, resLen = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and window[c] == countT[c]:
                Have += 1
                while Have == Need:
                    if (r-l+1) < resLen:
                        res = [r,l]
                        resLen = (r-l+1)
                    window[s[l]] -= 1
                    if s[l] in countT and window[s[l]] < countT[s[l]]:
                        Have -= 1
                    l += 1
        r,l = res
        return s[l:r+1] if resLen != float('inf') else ""