class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seq = 0
        max_seq = 0

        for num in nums:
            if num-1 not in nums:
                while num in nums:
                    seq += 1 
                    num += 1
                
            max_seq = max(seq, max_seq)
            seq = 0

        return max_seq

        

            