class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        print(count_nums)
        top_k_vals = sorted(count_nums.values())[-k:]
        print(top_k_vals)
        ret_lst = []
        for num in count_nums.keys():
            if count_nums[num] in top_k_vals:
                ret_lst.append(num)

        return ret_lst

        