class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            mid = top + ((bottom - top) // 2)
            #target is in middle row
            if matrix[mid][0] <= target and matrix[mid][len(matrix[mid])-1] >= target:
                for val in matrix[mid]:
                    if val == target:
                        return True
                return False
            #target is below middle row
            elif matrix[mid][0] > target:
                bottom = mid - 1
            #target is above middle row
            elif matrix[mid][0] < target:
                top = mid + 1
            
        return False
        