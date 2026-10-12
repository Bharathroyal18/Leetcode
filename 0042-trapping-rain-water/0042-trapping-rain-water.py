class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        count = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if height[left] < height[right]:
                water = leftMax - height[left]
                count = count + water
                left = left+1
            
            else:
                water = rightMax - height[right]
                count = count + water
                right = right-1
                
        return count