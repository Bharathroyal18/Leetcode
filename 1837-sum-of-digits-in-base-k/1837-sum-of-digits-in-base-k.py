class Solution:
    def sumBase(self, n: int, k: int) -> int:

        ans = 0

        while n > 0:
            val = n % k
            ans = ans + val
            n = n // k

        return ans
        