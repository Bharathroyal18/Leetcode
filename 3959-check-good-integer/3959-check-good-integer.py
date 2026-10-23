
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsum = 0
        squaresum = 0

        while n != 0:
            val = n % 10
            digitsum = digitsum + val
            squaresum = squaresum + val ** 2
            n = n // 10

        return squaresum - digitsum >= 50

        
        