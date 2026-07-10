class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumR = [nums[0]]
        for i in range(1, len(nums)):
                self.sumR.append(nums[i] + self.sumR[-1])
        print (self.sumR)

    def sumRange(self, left: int, right: int) -> int:
        diff = self.nums[left] - self.sumR[left]
        return (self.sumR[right] + diff)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)