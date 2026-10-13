class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text = s.split()[-1]
        return len(text)


        