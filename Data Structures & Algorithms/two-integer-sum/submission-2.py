class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_set = set()
        for idx in range(len(nums)):
            temp_set.add(nums[idx])
            num_2 = target-nums[idx]
            if num_2 in temp_set and nums.index(num_2) != idx:
                return sorted([idx, nums.index(num_2)])

