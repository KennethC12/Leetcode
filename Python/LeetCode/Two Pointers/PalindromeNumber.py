# Given an integer x, return true if x is a palindrome, and false otherwise.

# Approach:
# 1. Convert the integer to a string.
# 2. Use two pointers: L starts at the beginning, R at the end.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        s = str(x) # Convert the integer to a string

        l, r = 0, len(s) -1 # Use two pointers: L starts at the beginning, R at the end

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True