class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        currsum = 0
        d = {0: 1}

        for right in range(len(nums)):
            currsum = currsum +  nums[right]
            ans = currsum - goal

            if ans in d:
                count = count + d[ans]

            if currsum in d:
                d[currsum] = d[currsum] + 1
            else:
                d[currsum] = 1

        return count