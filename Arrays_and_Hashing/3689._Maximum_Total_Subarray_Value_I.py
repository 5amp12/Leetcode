class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        l = None
        r = None

        for num in nums:
            if l is None or num < l:
                l = num
           
            if r is None or num > r:
                r = num
           
        return (r - l) * k