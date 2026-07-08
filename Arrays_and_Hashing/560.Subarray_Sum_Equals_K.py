class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashSumArray = {0 : 1}
        currSubArrayVal = 0
        overall = 0
        for num in nums:
            currSubArrayVal += num
            if (currSubArrayVal - k) in hashSumArray:
                overall += hashSumArray[currSubArrayVal - k]

            if currSubArrayVal in hashSumArray:
                hashSumArray[currSubArrayVal] += 1
            else:
                hashSumArray[currSubArrayVal] = 1
        return overall

                