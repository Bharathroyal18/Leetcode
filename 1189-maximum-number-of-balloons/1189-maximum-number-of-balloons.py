class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}

        for i in range(len(text)):
            if text[i] in d:
                d[text[i]] = d[text[i]] + 1
            else:
                d[text[i]] = 1

        word = "balloon"
        count = float('inf')

        for key in word:
            required = 2 if key == 'l' or key == 'o' else 1
            count = min(count, d.get(key, 0) // required)

        return count
