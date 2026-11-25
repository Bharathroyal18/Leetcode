class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        left = 0
        count = 0

        freq = {'a': 0, 'b': 0, 'c': 0}
        for right in range(len(s)):
            freq[s[right]] = freq[s[right]] + 1
            
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                count=count+len(s)-right

                freq[s[left]] = freq[s[left]] - 1
                left = left + 1

        return count

        # count = 0
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         ans = s[i:j+1]

        #         if 'a' in ans and 'b' in ans and 'c' in ans:
        #             count = count + 1

        # return count