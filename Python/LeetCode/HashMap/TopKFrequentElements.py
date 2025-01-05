# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Approach:
# 1. Create a hashmap to store the frequency of each element in the array.
# 2. Create a list of lists to store the elements with the same frequency.
# 3. Iterate through the hashmap and add the elements to the corresponding frequency list.
# 4. Sort the frequency list in descending order.
# 5. Flatten the frequency list and return the first k elements.
# Time complexity: O(n log n)

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {} # Hashmap to store the frequency of each element
        for num in nums: # Iterate through the nums array
            count[num] = 1 + count.get(num, 0) # Increment the frequency of the element in the hashmap

        arr = [] # List of lists to store the elements with the same frequency
        for num, cnt in count.items(): # Iterate through the hashmap
            arr.append([cnt, num]) # Add the element and its frequency to the list
        arr.sort() # Then sort

        res = [] # List to store the top k frequent elements
        while len(res) < k: # Iterate until we have k elements
            res.append(arr.pop()[1]) # Add the element with the highest frequency to the result list
        return res # Finally, return the top k frequent elements
