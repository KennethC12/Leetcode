class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # So we have to convert all uppercase letters into lowercase letters
        # We will create two pointers L and R where we compare the the two pointers
        # If they dont match, Return False, otherwise return True

        # Convert all characters to lowercase and remove non-alphanumeric       characters
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        
        # Use two pointers: L starts at the beginning, R at the end
        L, R = 0, len(cleaned) - 1

        while L < R:
            if cleaned[L] != cleaned[R]:
                return False  # If characters don't match, it's not a palindrome
            L += 1  # Move L to the right
            R -= 1  # Move R to the left

        return True  # If all characters match, it's a palindrome