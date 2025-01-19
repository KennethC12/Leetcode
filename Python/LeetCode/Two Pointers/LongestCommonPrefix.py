class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        new = ""
        strs = sorted(strs) # Sort the Strings
        first, last = strs[0], strs[-1] # Initialze two pointers 
        for i in range(len(first)): 
            if i < len(last) and first[i] == last[i]:
                new += first[i]
            else:
                break
        return new