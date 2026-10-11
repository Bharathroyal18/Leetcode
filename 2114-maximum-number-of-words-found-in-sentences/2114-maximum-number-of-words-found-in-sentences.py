class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count = 0
        for i in range(len(sentences)):
            count = 0
            s = sentences[i]
            for j in range(len(s)):
                if s[j] == " ":
                    count = count + 1
            max_count = max(max_count, count + 1)
        return max_count