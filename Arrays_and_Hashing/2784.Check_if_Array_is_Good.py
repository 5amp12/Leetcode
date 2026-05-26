class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        n = len(nums) - 1

        for i in range(n):
            if nums[i] != i+1:
                return False

        return nums[n] == n
        