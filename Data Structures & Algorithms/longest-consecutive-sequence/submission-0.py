class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        i = 0
        visited = set()
        long_seq = 0

        while i < len(nums):
            if nums[i] in visited:
                i+=1
                continue

            num = nums[i]
            seq = 0
            while num in nums:
                visited.add(num)
                seq += 1
                num += 1

            long_seq = max(long_seq, seq)
            i+=1

        return long_seq

            