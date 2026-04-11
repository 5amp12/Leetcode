class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First find row target would be in, and assign left and right val and check

        #finding row
        targetRow = None
        lowRow, highRow = 0, len(matrix) - 1
        while lowRow <= highRow:
            midRow = (highRow + lowRow) // 2
            print(f"mid row {midRow}   l row {lowRow}  r row {highRow}")
            if matrix[midRow][0] <= target and matrix[midRow][len(matrix[midRow])-1] >= target:
                targetRow = midRow
                break
            elif target < matrix[midRow][0]:
                highRow = midRow - 1
            else:
                lowRow = midRow + 1
        print(targetRow)

        if targetRow == None:
            return False

        l, r = 0, len(matrix[targetRow])-1
        while l <= r:
            mid = (l+r) // 2
            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

