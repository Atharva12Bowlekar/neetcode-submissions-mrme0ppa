class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct_str = {}

        for str_ in strs:
            count_chrs = [0]*26

            for c in str_:
                count_chrs[ord(c) - ord("a")] += 1

            temp_str = tuple(count_chrs)
            if temp_str not in dct_str:
                dct_str[temp_str] = [str_]
            else:
                dct_str[temp_str].append(str_)

        return list(dct_str.values())
        