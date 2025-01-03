# Goal: Remove the duplicates in-place such that each element appear only once and return the new length.

# Example:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the returned length.
# Output: [1,2]

# Approach:
# 1. Uses a HashMap to store the unique elements in the array.
# 2. Iterate through the array and check if the element is in the HashMap.
# 3. If it is not, add it to the HashMap.
# 4. If it is, skip it.
# 5. Return the length of the HashMap.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = set()  # Use a set to track unique elements
        write_index = 0  # Pointer to overwrite elements in-place

        for num in nums:  # Loop through each element in the array
            if num not in seen:
                seen.add(num)  # Add the number to the seen set
                nums[write_index] = num  # Write the unique number in place
                write_index += 1  # Increment the pointer

        return write_index  # Return the new length of the modified array