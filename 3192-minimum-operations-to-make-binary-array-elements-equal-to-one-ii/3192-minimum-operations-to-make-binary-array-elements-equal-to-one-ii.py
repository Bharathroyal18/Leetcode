class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = 0
        flip = 0

        for i in range(len(nums)):
            if (nums[i] + flip) % 2 == 0:
                count = count + 1
                flip = flip + 1

        return count