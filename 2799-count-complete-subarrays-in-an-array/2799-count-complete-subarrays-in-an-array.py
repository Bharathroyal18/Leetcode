class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        left = 0
        ans = set()

        for right in range(len(nums)):
            ans.add(nums[right])

            while len(ans) == len(nums_set):
                count = count + len(nums) - right
                ans.remove(nums[left])
                left = left + 1

                for i in range(left, right + 1):
                    ans.add(nums[i])

        return count