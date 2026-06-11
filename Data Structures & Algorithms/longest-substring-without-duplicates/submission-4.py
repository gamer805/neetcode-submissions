class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        r=1
        seen = [s[0]]
        maxlen = 0
        while r < len(s):
            while s[r] in seen:
                seen = seen[1:]
            seen.append(s[r])
            r += 1
            maxlen = max(maxlen, len(seen))
        
        return maxlen
