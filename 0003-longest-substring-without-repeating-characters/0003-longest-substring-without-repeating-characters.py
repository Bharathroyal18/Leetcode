class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        ans=set()
        left=0
        for right in range(len(s)):
            if s[right] not in ans:
                ans.add(s[right])
                length=right-left+1
                max_length=max(max_length,length)
            else:
                while s[right] in ans:
                    ans.remove(s[left])
                    left+=1
            ans.add(s[right])
        return max_length
        