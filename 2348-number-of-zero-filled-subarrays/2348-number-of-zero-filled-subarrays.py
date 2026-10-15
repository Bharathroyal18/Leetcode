class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        streak = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                streak = streak+1
                count = count+streak
            else:
                streak = 0
        return count


        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if nums[j] == 0:
        #             count += 1
        #         else:
        #             break
        # return count


        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         sub = nums[i:j+1]
        #         if all(x == 0 for x in sub):         
        #             count += 1

        # return count