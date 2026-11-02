class Solution:
    def minMoves(self, nums: List[int]) -> int:
        low=min(nums)
        total=0
        for i in range(len(nums)):
            total=total+nums[i]-low
        
        return total