class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        opening = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack:
                    return False

                element = stack[-1]
                if char == opening[element]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0

                