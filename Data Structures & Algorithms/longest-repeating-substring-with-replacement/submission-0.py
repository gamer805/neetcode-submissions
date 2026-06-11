class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr_dict = {}
        l, r = 0, 1
        curr_dict[s[0]] = 1
        maxlen = 0
        while r < len(s):
            curr_dict[s[r]] = 1 + curr_dict.get(s[r], 0)
            if sum(curr_dict.values()) > max(curr_dict.values()) + k:
                print(sum(curr_dict.values()))
                curr_dict[s[l]] -= 1
                l += 1
            r += 1
            maxlen = max(maxlen, r-l)
        
        return maxlen
        

        