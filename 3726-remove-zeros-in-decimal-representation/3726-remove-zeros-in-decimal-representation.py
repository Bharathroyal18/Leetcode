class Solution:
    def removeZeros(self, n: int) -> int:
        ans=""
        while n!=0:
            val=n%10
            if val!=0:
                ans=str(val)+ans
            n=n//10
        return int(ans)
