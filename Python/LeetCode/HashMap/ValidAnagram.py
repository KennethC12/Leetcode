class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
#Original Idea
#I want to create an hashmap where it contains the strings, if the size of the string is the same then we contuine to check if the letters are the same as well, if not return false

#The optimal solution
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t) 
# it sorts the string if they are not identical then it returns false other wise returns true