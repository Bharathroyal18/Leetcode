class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total = sum(nums)
        minimum = min(nums)
        n = len(nums)

        return total - (n * minimum)