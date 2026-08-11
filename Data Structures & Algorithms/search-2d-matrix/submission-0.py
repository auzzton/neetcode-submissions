class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        total = m * n
        l = 0
        r = total - 1

        while l <= r:
            m = l + ((r - l) // 2)
            row = m // n #Formula
            col = m % n #Formula
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = m + 1
            else:
                r = m - 1
        return False