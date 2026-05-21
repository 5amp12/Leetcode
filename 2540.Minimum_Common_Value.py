class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1index, n2index = 0, 0
        while len(nums1) > n1index and len(nums2) > n2index:
            if nums1[n1index] == nums2[n2index]:
                return nums1[n1index]
            if nums1[n1index] > nums2[n2index]:
                n2index += 1
            else:
                n1index += 1

        return -1