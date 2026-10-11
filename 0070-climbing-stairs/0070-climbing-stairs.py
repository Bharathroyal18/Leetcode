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

        # For n = 3:

        #dry run for n=3

        # Start: a = 1, b = 2,       n = 3
        # c = 1 + 2 = 3
        # a = 2, b = 3
        # n = 2                    n=n-1[3-1=2] loop fails
        # 2 >= 3 is false, so stop.