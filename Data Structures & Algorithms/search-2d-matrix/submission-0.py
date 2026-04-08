class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num = 0
        for row_index, row in enumerate(matrix):
            if row[0] > target:
                break
            row_num = row_index

        nums = matrix[row_num]

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
        