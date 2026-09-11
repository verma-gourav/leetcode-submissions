class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_map = {}
        s_map = {}
        s_arr = s.split()

        if len(pattern) != len(s_arr):
            return False

        for c1, c2 in zip(pattern, s_arr):
            if c1 in pattern_map and pattern_map[c1] != c2:
                return False
            
            if c2 in s_map and s_map[c2] != c1:
                return False

            pattern_map[c1] = c2
            s_map[c2] = c1
        
        return True