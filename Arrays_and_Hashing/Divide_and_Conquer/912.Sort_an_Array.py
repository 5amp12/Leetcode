class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.divide(nums)

    def divide(self, nums):
        if len(nums) == 1:
            return nums
            
        mid = len(nums) // 2
        l = nums[:mid]
        r = nums[mid:]

        l = self.divide(nums[:mid])
        r = self.divide(nums[mid:])

        return self.merge(l, r)
    
    def merge(self, l, r):
    
        ovr = []
        rIndex = 0
        lIndex = 0
        while rIndex <= len(r)-1 and lIndex <= len(l)-1:
            if r[rIndex] > l[lIndex]:
                ovr.append(l[lIndex])
                lIndex += 1
            else:
                ovr.append(r[rIndex])
                rIndex += 1

        while rIndex <= len(r)-1:
            ovr.append(r[rIndex])
            rIndex += 1
        
        while lIndex <= len(l)-1:
            ovr.append(l[lIndex])
            lIndex += 1
            
        
        return ovr

        


        

