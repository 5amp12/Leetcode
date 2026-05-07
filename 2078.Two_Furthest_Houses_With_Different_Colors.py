class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = 0
        longestDisL = 0
        while l <= len(colors)-1:
            if colors[l] != colors[-1]:
                longestDisL = (len(colors)-1) - l
                break
            l+=1
        
        r = len(colors)-1
        longestDisR = 0
        while l <= r:
            if colors[r] != colors[0]:
                longestDisR = r - 0
                break
            r-=1
        
        return max(longestDisL, longestDisR)
            