class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        even=0
        odd=0
        for i in range(len(nums)):
            if i%2==0:
                even=even+nums[i]
            elif i==0:
                even=even+nums[i]
            else:
                odd=odd+nums[i]
        return even-odd
        