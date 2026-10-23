class Solution:
    def mirrorDistance(self, n: int) -> int:
        original=n
        ans=""
        while n!=0:
            val=n%10              
            ans=ans+str(val)
            n=n//10

        return abs(original-int(ans))
        