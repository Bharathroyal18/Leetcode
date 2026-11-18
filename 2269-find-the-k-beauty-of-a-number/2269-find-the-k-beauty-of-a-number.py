class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0

        window = s[:k]

        if int(window) != 0 and num % int(window) == 0:
            count = count + 1

        for i in range(k, len(s)):
            window = s[i-k+1:i+1]

            if int(window) != 0 and num % int(window) == 0:
                count = count + 1

        return count