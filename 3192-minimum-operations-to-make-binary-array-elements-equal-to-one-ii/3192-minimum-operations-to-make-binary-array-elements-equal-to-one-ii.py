class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        flip = 0

        for i in range(len(nums)):

            if flip % 2 == 1:
                if nums[i] == 0:
                    nums[i] = 1
                else:
                    nums[i] = 0

            if nums[i] == 0:
                count = count + 1
                flip = flip + 1

        return count