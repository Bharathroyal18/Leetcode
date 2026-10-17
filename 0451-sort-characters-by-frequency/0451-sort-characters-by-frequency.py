class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]=d[s[i]]+1
            else:
                d[s[i]]=1

        ans = ""

        for key,value in sorted(d.items(),key=lambda item: item[1], reverse=True):
            ans = ans+key * value

        return ans