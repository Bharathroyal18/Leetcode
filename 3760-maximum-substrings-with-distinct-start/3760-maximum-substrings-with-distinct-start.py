class Solution:
    def maxDistinct(self, s: str) -> int:

        count=0

        d={}
        for i in range(len(s)):
            if len(s) in d:
                d[s[i]]=d[s[i]]+1
            else:
                d[s[i]]=1

        for key in d:
            count=count+1
        
        return count
        