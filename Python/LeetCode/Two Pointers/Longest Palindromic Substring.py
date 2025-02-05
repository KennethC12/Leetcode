class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        cleaned = ''.join(c.lower() for c in s if c.isalnum()) # This removes non-alphanumeric characters
        n = len(cleaned)
        
        longest = ''
