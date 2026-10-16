class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        rev_arr = []

        for _ in range(len(arr)):
            rev_arr.append(arr.pop())
        
        return " ".join(rev_arr)
