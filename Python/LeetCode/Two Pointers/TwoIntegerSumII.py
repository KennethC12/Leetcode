# Example 1
# Input: numbers = [1,2,3,4], target = 3
# Output: [1,2]

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1  # Initialize two pointers

        while l < r:
            total = numbers[l] + numbers[r]  # Calculate the sum of the two numbers
            if total == target:
                return [l + 1, r + 1] # Return the indices of the two numbers
            elif total < target: # If the sum is less than the target
                l += 1 # Move the left pointer to the right
            else:
                r -= 1 # Move the right pointer to the left
        return [-1, -1] # If no solution is found, return [-1, -1]