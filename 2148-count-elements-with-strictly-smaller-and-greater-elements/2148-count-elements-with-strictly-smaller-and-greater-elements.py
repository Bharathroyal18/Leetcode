class Solution:
    def countElements(self, nums: list[int]) -> int:

        count=0

        smaller=min(nums)
        greater=max(nums)

        for i in range(len(nums)):
            if nums[i]<greater and smaller<nums[i]:
                count=count+1
        
        return count
        