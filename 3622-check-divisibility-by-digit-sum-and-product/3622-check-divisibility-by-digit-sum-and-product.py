class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n

        sum=0
        while n!=0:
            ans=n%10
            sum=sum+ans
            n=n//10

        n=original
        product=1
        while n!=0:
            val=n%10
            product=product*val
            n=n//10
        
        if original%(sum+product)==0:
            return True
        else:
            return False

        # return original % (sum + product) == 0

        
        