class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        for i in range(len(height)):
            if maxLeft == []:
                maxLeft.append(0)
            else:
                maxLeft.append(max(height[i-1],  maxLeft[-1]))

        maxRight = [0]
        for i in range(len(height) -2, -1, -1):
            if maxRight == []:
                maxRight.append(0)
            else:
                maxRight.append(max(height[i + 1], maxRight[-1]))
        maxRight = maxRight[::-1]
        
        minBoth = []
        waterTrapped = 0
        for i in range(len(maxLeft)):
            minBoth = min(maxLeft[i], maxRight[i])
            waterTrapped += max((minBoth - height[i]), 0)
        
        return waterTrapped

            

                        