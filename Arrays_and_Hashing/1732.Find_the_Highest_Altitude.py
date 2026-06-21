class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        highestAlt = 0
        for height in gain:
            alt += height
            highestAlt = max(highestAlt, alt)
        return highestAlt