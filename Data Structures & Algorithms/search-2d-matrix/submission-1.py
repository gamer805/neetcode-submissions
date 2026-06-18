class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix[-1][-1] < target or matrix[0][0] > target:
            return False

        row = int(len(matrix) / 2)
        b, t = 0, len(matrix)

        while t - b > 1 and not (matrix[row][0] <= target and matrix[row][-1] >= target):
            if matrix[row][0] > target:
                t = row
            elif matrix[row][-1] < target:
                b = row
            row = b + int((t-b)/2)

        if len(matrix[row]) == 1 and matrix[row][0] != target:
            return False
        
        l, r = 0, len(matrix[row])
        middle = int((r - l) / 2)
        while r - l > 1:
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                r = middle
            else:
                l = middle + 1
            middle = l+int((r - l) / 2)
            if middle >= len(matrix[row]):
                return False
        
        if matrix[row][middle] == target:
                return True
        
        return False