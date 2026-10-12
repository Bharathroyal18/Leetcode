class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        #return nums+nums[::-1]

        for i in range(len(nums)-1,-1,-1):
            nums.append(nums[i])
        return nums
        