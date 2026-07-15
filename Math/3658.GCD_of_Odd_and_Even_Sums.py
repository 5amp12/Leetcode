class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        sumOdd = 1
        sumEven = 2

        for i in range (1, n):
            sumOdd += 2
            sumEven += 2
        
        for i in range(n, -1, -1):
            print(i)
            if (sumOdd % i) == 0:
                return i
            if (sumEven % i) == 0:
                return i