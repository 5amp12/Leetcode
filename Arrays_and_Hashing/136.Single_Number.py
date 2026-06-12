class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = []

        for i in range(len(nums)):
            if nums[i] not in mapping:
                mapping.append(nums[i])
            else:
                mapping.remove(nums[i])
        
        return mapping[0]