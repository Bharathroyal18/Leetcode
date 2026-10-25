class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)

        sq = [x * x for x in nums]
        sq.sort(reverse=True)

        ans = 0
        pos = (n + 1) // 2
        for i in range(n):
            if i < pos:
                ans = ans + sq[i]
            else:
                ans = ans - sq[i]
                
        return ans