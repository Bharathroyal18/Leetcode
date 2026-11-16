class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        answer=n*(n+1)//2
        return (answer-total)
        