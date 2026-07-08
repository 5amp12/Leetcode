class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        index = 0
        for i in range(len(nums)):
                if nums[index] == 0:
                        nums.pop(index)
                        zeros.append(0)
                else:
                        index+=1
        nums.extend(zeros)