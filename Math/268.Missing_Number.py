class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        newset = set(nums)
        num_len = len(nums)
        for i in range(len(nums)+1):
                newset.add(i)
                if len(newset) > num_len:
                        return i