class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left=[]
        middle=[]
        right=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                left.append(nums[i])
            elif nums[i]==pivot:
                middle.append(nums[i])
            else:
                right.append(nums[i])
        return left+middle+right
        