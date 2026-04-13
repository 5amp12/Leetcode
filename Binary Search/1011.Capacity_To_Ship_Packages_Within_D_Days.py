class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowWeight, highWeight = max(weights), sum(weights)
        bestWeightCap = highWeight
        while lowWeight <= highWeight:
            midWeight = (lowWeight + highWeight) // 2
            currentDay, currentWeight = 1, 0
            for weight in weights:
                
                if (weight + currentWeight) <= midWeight:
                    currentWeight += weight
                else:
                    currentDay+=1
                    currentWeight = weight
                # print(f"weight: {weight}  currentDay: {currentDay}  currentWeight: {currentWeight}  middlecapWeight = {midWeight}")

            if currentDay > days:
                lowWeight = midWeight + 1
            else:
                if midWeight < bestWeightCap:
                    bestWeightCap = midWeight
                highWeight = midWeight - 1

        return bestWeightCap