class Solution:
    def pivotInteger(self, n: int) -> int:
        leftsum=0
        total = sum(range(1, n + 1))
        for i in range(1,n+1):
            rightsum=total-leftsum-i
            if rightsum==leftsum:
                return i
            leftsum=leftsum+i
        return -1

        