class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        midx = m - 1 # midx is the index of the last element of nums1
        nidx = n - 1 # nidx is the index of the last element of nums2
        right = m + n - 1 # right is the index of the last element of nums1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]: # if the last element of nums1 is greater than the last element of nums2
                nums1[right] = nums1[midx] # then we replace the last element of nums1 with the last element of nums1
                midx -= 1
            else:
                nums1[right] = nums2[nidx] # otherwise we replace the last element of nums1 with the last element of nums2
                nidx -= 1 # then we decrement the index of nums2

            right -= 1 # then we decrement the index of nums1