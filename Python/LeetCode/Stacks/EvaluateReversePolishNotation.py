# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Approach: Stacks
# 1. Iterate through the list of tokens
# 2. If the token is an operator, then pop the last two numbers from the stack
# 3. Perform the operation on the two numbers
# 4. Push the result back to the stack
# 5. If the token is a number, then push it to the stack
# 6. Return the last element of the stack
# Time complexity: O(n)


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(token))
        return stack[-1]