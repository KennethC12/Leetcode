class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0

        for p in range(len(nums)):
            if nums[p] != val:
                nums[k] = nums[p]
                k += 1


        return k