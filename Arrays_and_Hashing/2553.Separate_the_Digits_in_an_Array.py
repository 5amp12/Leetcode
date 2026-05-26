class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        indvNums = []
        for i in range(len(nums)):
            strNums = str(nums[i])
            for num in strNums:
                indvNums.append(int(num))
        
        return indvNums