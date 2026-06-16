class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []
        i = 0
        j = 0
        while j < len(temperatures):
            if i >= len(temperatures):
                result.append(0)
                stack = []
                j += 1
                i = j
            elif temperatures[i] > temperatures[j]:
                result.append(len(stack))
                stack = []
                j += 1
                i = j
            else:
                stack.append(temperatures[i])
                i += 1
        
        return result
        