# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Approach: 
# 1. Encode the strings by adding a length prefix to each string.
# 2. Concatenate the encoded strings with a delimiter.
# 3. Decode the strings by splitting the input string with the delimiter and extracting the length prefix.
# 4. Return the decoded strings.

class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}:{s}" for s in strs) # Encode the strings by adding a length prefix to each string
    def decode(self, s: str) -> List[str]:
        res = [] # List to store the decoded strings
        i = 0
        while i < len(s): # Iterate through the input string
            colon = s.find(':', i) # Find the colon delimiter
            length = int(s[i:colon]) # Extract the length prefix
            res.append(s[colon + 1:colon + 1 + length]) # Add the decoded string to the result list
            i = colon + 1 + length # Move the pointer to the next string
        return res