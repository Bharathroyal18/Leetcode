class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        original=x
        total=0
        while x!=0:
            val=x%10
            total=total+val
            x=x//10
        if original%total==0:
            return total
        else:
            return -1
        