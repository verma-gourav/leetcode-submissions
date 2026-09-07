class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        area = 0
        p1 = 0
        p2 = len(height) - 1

        while p1 < p2:
            min_height = min(height[p1], height[p2])
            curr_area = min_height * (p2 - p1)
            area = max(area, curr_area)

            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        
        return area