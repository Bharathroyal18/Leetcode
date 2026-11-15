class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        original=n
        product=1
        while n!=0:
            val=n%10
            product=product*val
            n=n//10
        
        n=original
        summ=0
        while n!=0:
            ans=n%10
            summ=summ+ans
            n=n//10
        
        return (product-summ)