# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Method:
# 1. Start from the end of the list
# 2. If the last digit is less than 9, then we can just increment it by 1 and return the list
# 3. If the last digit is 9, then we need to set the last digit to 0 and move to the next digit
# 4. If all the digits are 9, then we need to create a new list with 1 and the number of digits in the original list
# 5. Return the new list
# Time complexity: O(n)
# Space complexity: O(1)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = len(digits)

        for i in range(n-1, -1, -1): # start from the end of the list
            if digits[i] < 9: # if the last digit is less than 9
                digits[i] += 1 # then we can just increment it by 1
                return digits
            digits[i] = 0 # if the last digit is 9, then we need to set the last digit to 0 and move to the next digit
        
        return [1] + digits # if all the digits are 9, then we need to create a new list with 1 and the number of digits in the original list