class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b = 1, 2
        while n >= 3:
            c = a + b
            a = b
            b = c
            n =n-1

        return b