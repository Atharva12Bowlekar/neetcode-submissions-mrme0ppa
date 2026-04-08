class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct_str = {}

        for str_ in strs:
            temp_str = tuple(sorted(str_))
            if temp_str not in dct_str:
                dct_str[temp_str] = [str_]
            else:
                dct_str[temp_str].append(str_)

        ret_lst = []

        for value in dct_str.values():
            ret_lst.append(value)

        return ret_lst
        