class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:

        ans=max(arr)

        return arr.index(ans)      