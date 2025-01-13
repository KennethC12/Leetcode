# Example 1
# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(temperatures) # By * the len it will create a whole another list that only contains 0
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # stack[-1][0] means that it will access the last index of the list and then it will access the first element of that index
                stackT, stackInd = stack.pop() # Then removes the last element from the list
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res