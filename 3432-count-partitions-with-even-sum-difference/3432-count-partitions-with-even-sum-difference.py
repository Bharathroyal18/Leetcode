class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        leftsum=0
        total=sum(nums)
        for i in range(len(nums)-1):

            rightsum=total-leftsum
            if (leftsum-rightsum)%2==0:
                count=count+1
            
            leftsum=leftsum+nums[i]
        return count

        