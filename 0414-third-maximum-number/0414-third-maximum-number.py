class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans=set(nums)
        ans=sorted(ans,reverse=True)
        if len(ans)>=3:
            return(ans[2])
        else:
            return(ans[0])
    