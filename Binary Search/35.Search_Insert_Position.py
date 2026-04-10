class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r, = 0, len(nums)-1
        while l <= r:
            middle = (l+r) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                l = middle + 1
            elif target < nums[middle]:
                r = middle - 1

        
        return l
           