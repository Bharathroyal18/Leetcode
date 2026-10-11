class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1 = count1 + 1
            elif nums[i] == candidate2:
                count2 = count2 + 1
            elif count1 == 0:
                candidate1 = nums[i]
                count1 = count1 + 1
            elif count2 == 0:
                candidate2 = nums[i]
                count2 = count2 + 1
            else:
                count1 = count1 - 1
                count2 = count2 - 1

        count1 = nums.count(candidate1)
        count2 = nums.count(candidate2)
        ans = []
        if count1 > len(nums)//3:
            ans.append(candidate1)

        if count2 > len(nums)//3 and candidate2 != candidate1:
            ans.append(candidate2)
        return ans       