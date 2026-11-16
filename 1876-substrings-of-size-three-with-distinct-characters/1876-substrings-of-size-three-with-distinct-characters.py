class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            arr=s[i:i+3]
            if len(set(arr))==3:
                count=count+1
        return count
        