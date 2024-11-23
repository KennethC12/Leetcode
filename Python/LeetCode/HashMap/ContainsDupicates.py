class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}

        for nums in nums:
            if nums in seen:
                return True
            seen[nums] = 1 # This is adds the seen nums into the hashmap, the   value 1 is just a indicater that there is a dup or not.
        return False