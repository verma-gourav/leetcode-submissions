class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []
        paths = path.split("/")

        for char in paths:
            if char == "..":
                if stack:
                    stack.pop()
            elif char != "" and char != ".":
                stack.append(char)
        
        return "/" + "/".join(stack)
        