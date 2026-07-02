class Solution:
    def binarySearch(self, arr, target):
        l = 0
        h = len(arr)-1
        while l <= h:
            mid = (l + h) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # topRow = 0
        # lastRow = m-1
        # while topRow <= lastRow:
        #     midRow = (topRow + lastRow) // 2
        #     if target >= matrix[midRow][0] and target <= matrix[midRow][n-1]:
        #         return self.binarySearch(matrix[midRow], target)
        #     elif target < matrix[midRow][0]:
        #         lastRow = midRow - 1
        #     else:
        #         topRow = midRow + 1
        # return False
        # One pass
        l = 0
        r = m * n - 1
        while l <= r:
            mid = (l + r) // 2
            row, col = mid // n, mid % n
            # print("l : ",l," , r : ",r," , row : ",row," , col : ",col)
            if target < matrix[row][col]:
                r = mid - 1
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                return True
        return False
        