class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:

        count=0

        for i in range(len(patterns)):
            if patterns[i] in word:
                count=count+1

        return count
        