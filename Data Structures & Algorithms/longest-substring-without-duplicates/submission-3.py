class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in s[l:r]:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_len = max(max_len, len(s[l:r+1]))

        return max_len

