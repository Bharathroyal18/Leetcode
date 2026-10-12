class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        maximum=0
        while left<right:
            width=right-left
            length=min(height[left],height[right])
            area=width*length
            maximum=max(maximum,area)
            # maximum=max(maximum,(right-left)*min(height[left],height[right]))

            if height[left]<height[right]:
                left=left+1
            else:
                right-=1
        return maximum
        