class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = []

        # for i in range(len(nums)):
        #     left_side = nums[:i]
        #     left_product = 1
        #     for n in left_side:
        #         left_product *= n 

        #     right_side = nums[i + 1:]
        #     right_product = 1
        #     for n in right_side:
        #         right_product *= n
            
        #     res.append(left_product * right_product)
        
        # return res

        n = len(nums)
        product = [1] * n

        for i in range(1, len(nums)):
            product[i] = product[i - 1] * nums[i - 1]
        
        right = nums[-1]
        for i in range(n - 2, -1, -1):
            product[i] *= right
            right *= nums[i]
        
        return product

