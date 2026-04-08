class Solution:
    def checker(self, s_dict, t_dict):
        for key in t_dict.keys():
            if t_dict.get(key,0) > s_dict.get(key,0):
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        t_dict = Counter(t)
        min_val = ""
        min_res = float("infinity")
        for i in range(len(s)):
            for j in range(i, len(s)):
                mini_s = s[i:j+1]
                mini_s_dict = Counter(mini_s)
                if self.checker(mini_s_dict, t_dict) == True and min_res > len(mini_s):
                    min_res = min(min_res, len(mini_s))
                    min_val = mini_s
        return min_val
        