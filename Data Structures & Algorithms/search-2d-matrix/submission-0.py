class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Approach: concatenate the rows together, perform normal binary search on it.
        concat = []
        for row in matrix:
            concat += row
        
        left, right = 0, len(concat) - 1

        while left <= right:
            mid = (left + right) // 2
            if concat[mid] == target:
                return True
            
            if concat[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False