class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans=sum(nums)
        return ans%k
        