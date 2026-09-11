class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) <= 1:
            return [strs]
        
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1
            
            anagram_map[tuple(count)].append(s)
        
        return list(anagram_map.values())

