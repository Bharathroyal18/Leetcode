class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        if not nums:
            return ans

        start = nums[0]
        end = nums[0]

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                end = nums[i+1]

            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(end))

                start = nums[i+1]
                end = nums[i+1]

        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(end))
        return ans