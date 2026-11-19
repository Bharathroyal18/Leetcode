class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
    
        word = list(word)

        left = 0

        if ch in word:
            right = word.index(ch)
        else:
            right = -1

        # right = word.index(ch) if ch in word else -1

        
        if right == -1:
            return "".join(word)

        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        return "".join(word)