class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(n,2*n+1):
            if i%n==0 and i%2==0:
                return i

        #without loop
        # if n % 2 == 0:
        #     return n
        # else:
        #     return n * 2