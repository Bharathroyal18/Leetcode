class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        ans = 0
        for i in range(n):
            ans ^= start + 2 * i
        return ans

        # count=0
        # ans=0
        # for i in range(start,2*n,2):
        #     ans=ans^i
        #     if ans^i==0:
        #         count=0
        #     count=count+ans
        # return count

