class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c not in map:
                stack.append(c)
                continue
            if not stack or stack[-1] != map[c]:
                return False
            stack.pop()

        return not stack
