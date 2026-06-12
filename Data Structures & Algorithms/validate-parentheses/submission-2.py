class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = "{[("
        closers = "}])"
        corr_hash = {"[": "]", "{": "}", "(": ")"}

        for c in s:
            if c in openers:
                stack.append(c)
            elif len(stack) > 0 and c in closers and c == corr_hash[stack[-1]]:
                stack.pop()
            elif len(stack) > 0 or c not in closers or (c in closers and len(stack) == 0):
                return False
        return len(stack) == 0
        