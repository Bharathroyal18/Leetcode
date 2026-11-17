class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        ans = 0

        for i in range(1, k + 1):
            ans = (ans * 10 + 1) % k

            if ans == 0:
                return i

        return -1