class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        res_lst = [max(nums[l:r])]

        while r < len(nums):
            prev_max = res_lst[-1]
            l = l + 1
            r = l + k

            if nums[l-1] == prev_max:
                temp_sum = max(nums[l:r])
            else:
                temp_sum = max(prev_max, nums[r-1])
            res_lst.append(temp_sum)

        return res_lst

        