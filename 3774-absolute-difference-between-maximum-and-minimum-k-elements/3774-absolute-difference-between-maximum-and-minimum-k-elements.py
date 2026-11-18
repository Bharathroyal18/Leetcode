class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        lowest = sum(nums[:k])
        highest = sum(nums[-k:])
        return abs(highest - lowest)
        