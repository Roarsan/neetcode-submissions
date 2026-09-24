class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        rightMax = 0
        leftMax = 0
        trappedWater = 0

        while left < right:
            rightMax = max(height[right],rightMax)
            leftMax = max(height[left],leftMax)

            if height[left] <= height[right]:
                trappedWater += leftMax - height[left]

                left += 1
            else:
                trappedWater += rightMax - height[right]
                
                right -= 1
        return trappedWater
        