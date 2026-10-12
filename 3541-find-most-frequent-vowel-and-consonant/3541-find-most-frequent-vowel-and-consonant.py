class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]]=d[s[i]]+1
            else:
                d[s[i]]=1
        
        max_vowel=0
        for key in d:
            if key in "aeiou":
                if d[key]>max_vowel:
                    max_vowel=d[key]
        
        max_consonant=0
        for key in d:
            if key not in "aeiou":
                if d[key]>max_consonant:
                    max_consonant=d[key]

        ans=max_vowel+max_consonant

        return ans
        