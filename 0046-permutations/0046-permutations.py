class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        seen = set()

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num in seen:
                    continue
                
                curr.append(num)
                seen.add(num)

                backtrack(curr)

                curr.pop()
                seen.remove(num)

        backtrack([])       
        return res