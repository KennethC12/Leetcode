class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        prevMap = {}

#So we are going to create a hashmap that will contain the list of nums and we will create a for loop that will find the difference which is going to be the target minus n, and if that difference is in the hashmap then it will then just return the difference and the original num that added up to the target.

        for i, n in enumerate(nums): #Enumerate adds a index to the nums
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i  
        return