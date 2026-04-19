class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        smallestLen = None
        l = 0
        overallSum = 0
        for r in range(len(nums)):
            overallSum += nums[r]
            print(f"before l {nums[l]}  r  {nums[r]}  overall = {overallSum}")
            while overallSum >= target:
                if smallestLen == None or ((r-l)+1) < smallestLen:
                    smallestLen = (r-l)+1
                overallSum -= nums[l]
                l+=1
    
                
        return smallestLen or 0