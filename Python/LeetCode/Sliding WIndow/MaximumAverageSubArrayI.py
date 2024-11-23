class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)  
        cur_sum = sum(nums[:k])
       
        max_avg = float(cur_sum) / k

      
        for i in range(k, n):
            cur_sum += nums[i]  
            cur_sum -= nums[i - k]  
            avg = float(cur_sum) / k  
            max_avg = max(max_avg, avg)  

        return max_avg