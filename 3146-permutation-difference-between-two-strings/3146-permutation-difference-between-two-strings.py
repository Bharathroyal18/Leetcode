class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d= {}
        for i in range(len(t)):
            d[t[i]] = i

        ans = 0
        for i in range(len(s)):
            ans = ans + abs(i - d[s[i]])
            
        return ans