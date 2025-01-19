class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.
        Uses the sliding window technique with a set to track unique characters.
        """
        
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Stores the length of the longest substring found
        char_set = set()  # Set to store unique characters in the current window
        
        # Iterate over each character in the string with the right pointer
        for right in range(len(s)):
            # If the current character is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])  # Remove the leftmost character from the set
                left += 1  # Move the left pointer forward
            
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update max_length with the size of the current window
            max_length = max(max_length, right - left + 1)
        
        return max_length  # Return the maximum length found
