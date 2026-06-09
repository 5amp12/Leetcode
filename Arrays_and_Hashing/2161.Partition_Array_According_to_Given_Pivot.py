class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lPiv = []
        piv = []
        rPiv = []
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] > pivot:
                rPiv.append(nums[i])
            elif nums[i] < pivot:
                lPiv.append(nums[i])
            else:
                piv.append(nums[i])
        
        return lPiv + piv + rPiv

