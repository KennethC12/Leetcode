class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sign = -1 if x < 0 else 1  # remember sign
        x = abs(x)                 # work with positive value

        # Reverse the string representation
        rev_str = str(x)[::-1]

        # Convert back to integer with the original sign
        rev_int = sign * int(rev_str)

        # 32-bit overflow check
        if rev_int < -2**31 or rev_int > 2**31 - 1:
            return 0

        return rev_int
