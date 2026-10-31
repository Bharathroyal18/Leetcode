class Solution:
    def trap(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        count=0
        leftmax=0
        rightmax=0
        while left<right:
            leftmax=max(leftmax,height[left])
            rightmax=max(rightmax,height[right])

            if leftmax<rightmax:
                count=count+(leftmax-height[left])
                left=left+1
            
            else:
                count=count+(rightmax-height[right])
                right=right-1

        return count