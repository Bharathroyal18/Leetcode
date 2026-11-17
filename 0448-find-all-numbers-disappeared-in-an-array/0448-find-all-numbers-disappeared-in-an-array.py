class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        val=set(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in val:
                ans.append(i)
        return ans