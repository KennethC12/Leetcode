# O(log n)
# Goal: Given a sorted array a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# Example:
# Input: [1,3,5,6], 5
# Output: 2


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Find the middle index
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        return left  # Target not found, return the insertion position