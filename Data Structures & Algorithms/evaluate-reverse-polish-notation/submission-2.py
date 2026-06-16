class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "*/+-"
        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                n, m = stack[-2], stack[-1]
                stack.pop()
                stack.pop()
                if c == "+":
                    stack.append(n+m)
                elif c == "-":
                    stack.append(n-m)
                elif c == "*":
                    stack.append(n*m)
                elif c == "/":
                    stack.append(int(n/m))
        
        return stack[-1]
            