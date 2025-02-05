class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: # Base case
            return []
        if numRows == 1: # Base case
            return [[1]]

        prev_rows = self.generate(numRows - 1) # Recursive call
        prev_row = prev_rows[-1] # Get the last row
        current_row = [1] # Initialize the current row

        for i in range(1, numRows - 1): # Fill the current row
            current_row.append(prev_row[i - 1] + prev_row[i]) # Add the two numbers from the previous row

        current_row.append(1) # Add the last number
        prev_rows.append(current_row) # Add the current row to the list

        return prev_rows