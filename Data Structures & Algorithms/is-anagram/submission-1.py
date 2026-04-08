class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = Counter(s)
        dict_t = Counter(t)

        if len(dict_s) != len(dict_t):
            return False

        for key in dict_s.keys():
            if dict_s[key] != dict_t[key]:
                return False
        return True