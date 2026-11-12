class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase = 1
        decrease = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increase = increase + 1
                decrease = 1

            elif nums[i] < nums[i-1]:
                decrease = decrease + 1
                increase = 1

            else:
                increase = 1
                decrease = 1

            ans = max(ans, increase, decrease)

        return ans