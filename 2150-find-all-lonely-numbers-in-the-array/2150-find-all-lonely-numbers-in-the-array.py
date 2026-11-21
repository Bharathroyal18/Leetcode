class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:

        ans=[]

        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]=d[nums[i]]+1
            else:
                d[nums[i]]=1
        
        for key in d:
            if d[key]==1:
                 if key - 1 not in d and key + 1 not in d:
                    ans.append(key)
        
        return ans