class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        maxAmount = 0
        while left < right:

            if heights[left] <= heights[right]:
                minHeight = min(heights[left],heights[right])

                width = right- left

                amount = width * minHeight

                left += 1
            elif heights[left] > heights[right]:
                minHeight = min(heights[left],heights[right])

                width = right- left

                amount = width * minHeight
                right -= 1
            else:
                break


            

            maxAmount = max(amount,maxAmount)
        return maxAmount










            
            
            


        