class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        ans = 0
        left = 0
        prefix = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd_count = odd_count+1
                prefix = 0

            while odd_count == k:
                prefix = prefix+1
                if nums[left] % 2 != 0:
                    odd_count = odd_count-1
                left = left+1

            ans = ans+prefix

        for n in range(len(nums)):
            if nums[n] % 2 != 0:
                break
        else:
            return 0

        return ans