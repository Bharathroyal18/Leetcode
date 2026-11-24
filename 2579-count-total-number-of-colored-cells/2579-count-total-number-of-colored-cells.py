class Solution:
    def coloredCells(self, n: int) -> int:

        total=1

        for i in range(1,n):
            total=total+4*i

        return total

        # return 2*n*(n-1)+1
        