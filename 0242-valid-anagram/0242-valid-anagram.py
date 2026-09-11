class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        #------------------------------------------#

        # return sorted(s) == sorted(t)

        #------------------------------------------#

        # count = {}

        # for char in s:
        #     count[char] = count.get(char, 0) + 1
        
        # for char in t:
        #     if char not in count or count[char] == 0:
        #         return False
            
        #     count[char] -= 1
        #     if count[char] == 0:
        #         del count[char]
            
        # return len(count) == 0

        #------------------------------------------#

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
        
        for c in count:
            if c != 0:
                return False
        
        return True

