class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dct = {}

        for i, num in enumerate(nums):
            prt = target - num
            if prt in temp_dct:
                return [temp_dct[prt], i]
            temp_dct[num] = i
            

