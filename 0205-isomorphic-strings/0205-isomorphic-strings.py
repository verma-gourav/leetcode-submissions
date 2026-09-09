class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        map_st, map_ts = {}, {}

        for c1, c2 in zip(s, t):
            # s -> t map check
            if c1 in map_st and map_st[c1] != c2:
                return False
            
            # t -> s map check
            if c2 in map_ts and map_ts[c2] != c1:
                return False
            
            map_st[c1] = c2
            map_ts[c2] = c1
        
        return True
                    
