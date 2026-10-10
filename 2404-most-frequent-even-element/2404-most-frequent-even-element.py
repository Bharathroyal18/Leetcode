
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] = d[nums[i]] + 1
            else:
                d[nums[i]] = 1

        even = {}
        for key in d:
            if key % 2 == 0:
                even[key] = d[key]

        if not even:
            return -1

        max_freq = max(even.values())
        ans = []
        for key in even:
            if even[key] == max_freq:
                ans.append(key)

        ans = min(ans)
        return ans