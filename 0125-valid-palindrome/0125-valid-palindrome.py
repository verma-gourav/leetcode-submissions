class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_arr = [char.lower() for char in s if char.isalnum()]
        
        l, r = 0, len(s_arr) - 1
        while l <= r:
            if s_arr[l] != s_arr[r]:
                return False
            l += 1
            r -= 1
        return True