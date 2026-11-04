class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.sort()

        target = 1
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] == target:
                target = target + 1
            elif nums[i] > target:
                return target
        
        return target
        