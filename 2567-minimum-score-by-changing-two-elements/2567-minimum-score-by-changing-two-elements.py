class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        
        nums.sort()

        a = nums[-1] - nums[2]
        b = nums[-2] - nums[1]
        c = nums[-3] - nums[0]

        return min(a, b, c)