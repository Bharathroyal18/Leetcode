class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        even=0
        odd=0
        for i in range(len(s)):
            if i%2==0:
                even=even+int(s[i])
            elif i==0:
                even=even+int(s[i])
            else:
                odd=odd+int(s[i])
        return even-odd

        