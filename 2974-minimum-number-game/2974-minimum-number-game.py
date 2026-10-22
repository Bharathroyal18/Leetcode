class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while nums:
            first = min(nums)
            nums.remove(first)

            second = min(nums)
            nums.remove(second)

            arr.append(second)
            arr.append(first)

        return arr