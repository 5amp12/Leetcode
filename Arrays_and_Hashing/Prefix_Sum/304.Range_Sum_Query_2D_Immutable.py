class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMat = matrix

        for i in range(len(matrix)):
            for x in range(len(matrix[i])):
                if x != 0:
                    self.sumMat[i][x] += self.sumMat[i][x-1]
                
                if i != 0: 
                    self.sumMat[i][x] += self.sumMat[i-1][x]
                    if x != 0:
                        self.sumMat[i][x] -= self.sumMat[i-1][x-1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.sumMat[row2][col2]
        if row1 == 0:
            above = 0
        else:
            above = self.sumMat[row1-1][col2]
        
        if col1 == 0:
            left = 0
        else:
            left = self.sumMat[row2][col1-1]
        
        if col1 == 0 or row1 == 0:
            topLeft = 0
        else:
            topLeft = self.sumMat[row1-1][col1-1]

        return bottomRight - above - left + topLeft


        
        return ovr


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)