class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        s = list(set(nums))

        if min(s) < k:
            return -1

        count = 0

        for i in range(len(s)):
            if s[i] > k:
                count += 1

        return count