class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)

            squared_sum = 0
            while n > 0:
                digit = n % 10
                squared_sum += digit * digit
                n = n // 10
            n = squared_sum
        
        return n == 1
