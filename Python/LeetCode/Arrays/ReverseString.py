class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # This splits the string into words
        s = s.split()
        # Then this reverse the strings
        s = s[::-1]
        # Then join the words
        return ' '.join(s)