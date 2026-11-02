class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        moves=0
        mid=nums[len(nums)//2]
        for i in range(len(nums)):
            moves=moves+abs(nums[i]-mid)

        return moves
        