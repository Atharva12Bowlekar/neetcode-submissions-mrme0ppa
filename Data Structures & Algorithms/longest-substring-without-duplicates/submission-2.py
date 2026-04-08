class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub_str = ''
        max_len = 0

        for r in range(len(s)):
            while s[r] in s[l:r]:
                l += 1
            max_len = max(max_len, len(s[l:r+1]))
        return max_len