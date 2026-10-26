class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            current_lcm = 1

            for j in range(i, len(nums)):
                current_lcm = lcm(current_lcm, nums[j])

                if current_lcm == k:
                    count = count + 1

        return count