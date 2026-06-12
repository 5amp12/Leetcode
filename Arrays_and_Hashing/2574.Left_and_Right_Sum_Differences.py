class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        numLength = len(nums)
        ans = [0]

        leftSum = 0
        for i in range(numLength-1):
            leftSum += nums[i]
            ans.append(leftSum)
                
        rightSum = 0
        for i in range(numLength -1, -1, -1):
            ans[i] = abs(ans[i] - rightSum)
            rightSum += nums[i]
    
        return ans