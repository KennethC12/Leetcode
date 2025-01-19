class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        i , j = 0, len(s) -1 # Initialze Two pointers 

        vowels = set("aeiouAEIOU") # Create a hashmap that contains the vowels

        while (i<j):
            if (s[i] not in vowels):
                i+=1
            elif(s[j] not in vowels):
                j-=1
            else:
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1

        return "".join(s)