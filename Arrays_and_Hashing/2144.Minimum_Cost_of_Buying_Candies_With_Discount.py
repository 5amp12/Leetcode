class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost)
        overallAmount = 0

        i = len(cost) -1
        while i >= 0:
            overallAmount += cost[i]
            if i-1 >= 0:
                overallAmount += cost[i-1]
            i -= 3
        
        return overallAmount