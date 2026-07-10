class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftIndex = [0]
        for i in range(len(nums)):
            leftIndex.append(leftIndex[-1] + nums[i])
            
        rightIndex = [0] * (len(nums))
        for i in range(len(nums) -1, -1, -1):
            if i != len(nums)-1:
                print(rightIndex[i+1])
                rightIndex[i] = (rightIndex[i+1] + nums[i+1])
                    
        for i in range(len(nums)):
            if rightIndex[i] == leftIndex[i]:
                return i
        return -1