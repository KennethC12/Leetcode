# So we have nums[i], nums[j], nums[k] and we need to find the sum of these three numbers that is equal to 0.

# Method: Two Pointers
# 1. Sort the list
# 2. Iterate through the list
# 3. If the current number is greater than 0, then we can break the loop because we can't find a sum that is equal to 0
# 4. If the current number is the same as the previous number, then we can skip it because we have already calculated the sum for that number
# 5. We set the left pointer to i + 1 and the right pointer to the end of the list
# 6. We calculate the sum of the three numbers
# 7. If the sum is less than 0, then we increment the left pointer
# 8. If the sum is greater than 0, then we decrement the right pointer
# 9. If the sum is equal to 0, then we add the three numbers to the result list
# 10. We need to skip the duplicates
# 11. Return the result list
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1 # left pointer and right pointer, The left pointer is set to i + 1 and the right pointer is set to the end of the list

            while l < r: # while left pointer is less than right pointer
                three_sum = a + nums[l] + nums[r] # calculate the sum of the three numbers
                if three_sum > 0: # If the sum is greater than 0
                    r -= 1 # decrement the right pointer
                elif three_sum < 0: # If the sum is less than 0
                    l += 1 # increment the left pointer
                else: # If the sum is equal to 0
                    res.append([a, nums[l], nums[r]]) # add the three numbers to the result list
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # skip the duplicates
                        l += 1
        return res