class Solution:
    def minMoves(self, nums: List[int]) -> int:
        high=max(nums)
        total_moves=0
        for i in range(len(nums)):
            total_moves=total_moves+(high-nums[i])

        return total_moves        