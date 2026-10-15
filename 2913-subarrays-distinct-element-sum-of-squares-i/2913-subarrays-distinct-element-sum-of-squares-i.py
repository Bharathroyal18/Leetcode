class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                distinct = set(nums[i:j+1])
                count = count + len(distinct) ** 2
        return count
        