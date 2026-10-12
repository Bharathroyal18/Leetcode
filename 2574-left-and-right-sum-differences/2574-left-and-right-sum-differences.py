class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        leftsum=0
        for i in range(len(nums)):
            rightsum=sum(nums[i+1:])
            ans.append(abs(leftsum-rightsum))
            leftsum=leftsum+nums[i]
        return ans