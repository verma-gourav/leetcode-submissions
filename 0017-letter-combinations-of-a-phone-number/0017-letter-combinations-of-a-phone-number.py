class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            
            for char in mapping[digits[i]]:
                backtrack(i + 1, curr_str + char)

        if digits:
            backtrack(0, "") 

        return res           
