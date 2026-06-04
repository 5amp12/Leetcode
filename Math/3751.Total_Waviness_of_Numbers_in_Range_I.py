class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        waves = 0
        for num in range(num1, num2+1):
            numstr = str(num)
            for indvNum in range(len(numstr)):
                if indvNum == 0 or indvNum == len(numstr)-1:
                    continue
                
                if numstr[indvNum - 1] > numstr[indvNum] and numstr[indvNum + 1] > numstr[indvNum]:
                    waves +=1
                elif numstr[indvNum - 1] < numstr[indvNum] and numstr[indvNum + 1] < numstr[indvNum]: 
                    waves+=1

        return waves