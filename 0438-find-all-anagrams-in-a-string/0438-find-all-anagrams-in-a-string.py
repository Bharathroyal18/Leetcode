class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        d={}
        for i in range(len(p)):
            if p[i] in d:
                d[p[i]]=d[p[i]]+1
            else:
                d[p[i]]=1
        k=len(p)
        if k > len(s):
            return []
        window={}
        for i in range(k):
            if s[i] in window:
                window[s[i]]=window[s[i]]+1
            else:
                window[s[i]]=1

        ans=[]
        if window == d:
            ans.append(0)
        for i in range(k,len(s)):
            window[s[i-k]]= window[s[i-k]]-1
            if window[s[i-k]] == 0:
                del window[s[i-k]]

            window[s[i]]= window.get(s[i],0)+1
            if window==d:
                ans.append(i-k+1)
        return ans