class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        n = len(s)
        i = n - 1

        while i >= 0:
            while i>= 0 and s[i] == " ":
                i -= 1
            
            if i < 0: break

            word = []
            while i >= 0 and s[i] != " ":
                word.append(s[i])
                i -= 1
            
            left, right = 0, len(word) - 1
            while left < right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            
            words.append("".join(word))
        
        return " ".join(words)