class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while len(s[l:r+1]) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(len(s[l:r+1]), res)
        return res