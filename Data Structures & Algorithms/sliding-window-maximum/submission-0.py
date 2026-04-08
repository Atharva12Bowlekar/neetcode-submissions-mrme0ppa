class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        res_lst = []

        while r <= len(nums):
            temp_sum = max(nums[l:r])
            res_lst.append(temp_sum)

            l = l + 1
            r = l + k

        return res_lst

        