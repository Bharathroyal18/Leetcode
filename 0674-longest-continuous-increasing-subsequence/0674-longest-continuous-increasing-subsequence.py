class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=1
        max_count=1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                count+=1
            else:
                count=1
            max_count=max(count,max_count)

        return max_count
        