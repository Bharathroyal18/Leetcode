class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        d={}
        max_length=0
        for right in range(len(s)):
            if s[right] in d:
                d[s[right]]=d[s[right]]+1
            else:
                d[s[right]]=1
            ans=(right-left+1)-max(d.values())       #window_length - max_freq


            while ans>k:
                d[s[left]]=d[s[left]]-1
                left=left+1
                ans = (right - left + 1) - max(d.values())

            length=right-left+1
            max_length=max(max_length,length)
            
        return max_length
