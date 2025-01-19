class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * (len(nums)) # Create a result array that contains 1's and it is going to be the same length as the nums array

        # Initialize prefix to 1. This will hold the product of all elements
        # to the left of the current index as we iterate forward.
        prefix = 1

        # First pass: fill 'res' such that res[i] contains the product of
        # all elements to the left of i (i.e., prefix).
        for i in range(len(nums)):
            # Assign the current prefix product to res[i]
            res[i] = prefix
            # Update prefix to include nums[i]
            prefix *= nums[i]

        # Initialize postfix to 1. This will hold the product of all elements
        # to the right of the current index as we iterate backward.
        postfix = 1

        # Second pass (in reverse): multiply each res[i] by the postfix product,
        # which is the product of all elements to the right of i.
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the existing value in res[i] by the current postfix
            res[i] *= postfix
            # Update postfix to include nums[i]
            postfix *= nums[i]

        # By now, res[i] holds the product of all elements except nums[i].
        return res

