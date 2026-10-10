class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maximum=0
        while left<right:
            width=right-left
            area=width*min(height[left],height[right])
            maximum=max(maximum,area)
            if height[left]<height[right]:
                left=left+1
            else:
                right-=1
        return maximum
        