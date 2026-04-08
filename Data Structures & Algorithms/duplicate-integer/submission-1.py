class Solution:
    from collections import Counter
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_nums = Counter(nums)

        for value in dict_nums.values():
            if value > 1:
                return True
        return False