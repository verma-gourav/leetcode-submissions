class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, curr):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            if sum(curr) > target:
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr)
                curr.pop()
        
        backtrack(0, [])
        return res
