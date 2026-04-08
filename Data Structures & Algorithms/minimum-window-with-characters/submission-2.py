from collections import Counter

class Solution:
    def checker(self, s_dict, t_dict):
        for key in t_dict:
            if t_dict[key] > s_dict.get(key, 0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        min_val = ""
        min_res = float("inf")

        l = 0
        for r in range(len(s)):
            mini_s = Counter(s[l:r+1])

            while self.checker(mini_s, t_dict):
                window_len = r - l + 1
                if window_len < min_res:
                    min_res = window_len
                    min_val = s[l:r+1]

                l += 1
                mini_s = Counter(s[l:r+1])

        return min_val
