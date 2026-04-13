class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallestNum = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                smallestNum = min(smallestNum, nums[l])
            
            mid = (l + r) // 2
            smallestNum = min(smallestNum, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        return smallestNum