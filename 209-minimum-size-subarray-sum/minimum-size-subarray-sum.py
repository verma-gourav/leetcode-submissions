class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len = float("inf")
        curr_sum = 0
        p1, p2 = 0, 0

        for p2 in range(len(nums)):
            curr_sum += nums[p2]

            while curr_sum >= target:
                min_len = min(min_len, p2 - p1 + 1)
                curr_sum -= nums[p1]
                p1 += 1
        
        return min_len if min_len != float("inf") else 0
