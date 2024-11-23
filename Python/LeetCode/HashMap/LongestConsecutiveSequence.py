class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #We put the list into a hashmap, then we organize the hashmap, with the organized hashmap, we can tell which is a sequence or not

        numset = set(nums)
        longest = 0 # This is 0 because there is no current sequence yet
        
        for n in nums:
            # We make a if statement to check if there is even a sequence
            if (n-1) not in numset: # n - 1 means that if 4 - 1 = 3, we will see if 3 is in the numset
                length = 0

                while (n + length) in numset: # if 4 + 0 is in the numset the length += 1
                    length += 1
                longest = max(length, longest) # The max function takes the max of those two and makes longest the max

        return longest # Then return the output
        