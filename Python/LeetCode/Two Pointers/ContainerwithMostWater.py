class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # We are going to use two pointers, with the two pointers we will find which two are the largest   height and we will just multiply the left and right pointer


        res = 0 # make the results 0 for now
        L,R = 0, len(height) - 1 # Now we have the left and right pointers

        while L < R:
            area = (R - L) * min(height[L], height[R])
            res = max(res, area)

            if height[L] < height[R]:
                L+= 1
            else:
                R-= 1

        return res
                
