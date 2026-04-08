class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        lst_freqs = [[] for _ in range(len(nums)+1)]

        for num, count in count_nums.items():
            lst_freqs[count].append(num)

        ret_lst = []
        for i in range(len(lst_freqs)-1, -1, -1):
            for num in lst_freqs[i]:
                ret_lst.append(num)
                if len(ret_lst) == k:
                    return ret_lst