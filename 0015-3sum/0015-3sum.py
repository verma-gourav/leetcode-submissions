class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        res = []
        nums.sort()

        for i in range(len(nums)):
            # skip duplicates for 1st element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            p1 = i + 1
            p2 = len(nums) - 1
            
            while p1 < p2:
                curr_sum = nums[i] + nums[p1] + nums[p2]
                if curr_sum == 0:
                    res.append([nums[i], nums[p1], nums[p2]])
                    
                    # skip duplicates for p1 and p2
                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                        
                    p1 += 1
                    p2 -= 1
                elif curr_sum > 0:
                    p2 -= 1
                else:
                    p1 += 1
        
        return res
