class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count=0

        for i in range(len(nums)):
            if nums[i]==1:
                continue

            if i+2<len(nums):
                nums[i]=1-nums[i]
                nums[i+1]=1-nums[i+1]
                nums[i+2]=1-nums[i+2]
            
                count=count+1
            else:
                return -1
        
        return count
        