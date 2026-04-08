class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            num_2 = target-nums[idx]
            if num_2 in nums and nums.index(num_2) != idx:
                return sorted([idx, nums.index(num_2)])

