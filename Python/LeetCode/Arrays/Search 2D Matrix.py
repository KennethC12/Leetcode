class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix or not matrix[0]: #  Not in matrix then False
            return False
    
        m = len(matrix) # Columns
        n = len(matrix[0]) # Rows
        
        low, high = 0, m * n - 1 #  Low and High
        
        while low <= high:
            mid = (low + high) // 2 #  Mid
            row = mid // n #  Row
            col = mid % n #  Col
            
            if matrix[row][col] == target: #  Found
                return True
            elif matrix[row][col] < target: #  Target is greater
                low = mid + 1
            else:
                high = mid - 1
        
        return False