class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        op = ["+", "-", "*", "/"]
        
        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                match token:
                    case "+":
                        stack.append(val2 + val1)
                    case "-":
                        stack.append(val2 - val1)
                    case "*":
                        stack.append(val2 * val1)
                    case "/":
                        stack.append(int(val2 / val1))
                    case _:
                        return -1
        
        return stack[-1]


                