class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        curr_sum=0
        min_length=float('inf')
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>=target:
                length=right-left+1
                min_length=min(min_length,length)

                curr_sum=curr_sum-nums[left]
                left+=1
        if min_length==float('inf'):
            return 0
        return min_length

