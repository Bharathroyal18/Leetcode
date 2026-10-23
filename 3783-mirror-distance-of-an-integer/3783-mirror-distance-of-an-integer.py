class Solution:
    def mirrorDistance(self, n: int) -> int:
        original=n
        ans=""
        while n!=0:
            val=n%10              
            ans=ans+str(val)
            n=n//10

        return abs(original-int(ans))

        # ans = int(str(n)[::-1])
        # return abs(n - ans)
        