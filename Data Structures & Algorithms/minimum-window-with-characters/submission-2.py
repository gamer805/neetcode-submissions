class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        if s == t: return s
        if t in s: return t
        elif len(t) == 1: return ""

        t_hash = {}
        for c in t:
            t_hash[c] = 1 + t_hash.get(c, 0)
        print(t_hash)
        
        l, r = 0, 1

        map_hash = {}
        if s[l] in t_hash: map_hash[s[l]] = 1
        minstr = s + " "
        while r < len(s):
            if s[r] in t_hash: map_hash[s[r]] = 1 + map_hash.get(s[r], 0)
            while all(k in map_hash and map_hash[k] >= t_hash[k] for k in t_hash):
                if len(minstr) > r-l+1: minstr = s[l:r+1]
                if s[l] in t_hash: map_hash[s[l]] -= 1
                l += 1
            r += 1
        if len(minstr) > len(s): return ""
        return minstr
        