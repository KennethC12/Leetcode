class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #

        l, r = 0 , 1 # left = buy, right = sell 
        maxp = 0 # current max profit

        while r < len(prices): # while right pointer is less than the length of prices
            if prices[l] < prices[r]: # if left price is less than right price
                # Then we calculate the profit
                profit = prices[r] - prices[l]
                # Then we find the max profit 
                maxp = max(maxp, profit)
            else:
                l = r # You want to make l the min
            r += 1 # then you iterate it until it reaches the end of the list

        return maxp
