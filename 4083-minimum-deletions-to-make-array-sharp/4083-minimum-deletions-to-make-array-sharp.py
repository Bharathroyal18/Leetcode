class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        deletion=0
        prev=None
        for i in range(len(nums)):
            if prev==nums[i]:
                deletion=deletion+1
            else:
                prev=nums[i]
        return deletion
        