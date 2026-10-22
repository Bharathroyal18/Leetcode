class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]=d[nums[i]]+1
            else:
                d[nums[i]]=1
        ans=[]
        for key in d:
            if d[key]>1:
                ans.append(key)
        
        return ans
        