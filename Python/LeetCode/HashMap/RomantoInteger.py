# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# nput: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        prev = 0

        for i in range(len(s) - 1, -1, -1):
            curr = roman[s[i]]
            if curr < prev:
                res -= curr
            else:
                res += curr
            prev = curr
        return res