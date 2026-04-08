class Solution:
    

    def encode(self, strs: List[str]) -> str:
        s = ""
        for str_ in strs:
            s += str(len(str_)) + "-" + str_
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        j = i
        ret_lst = []
        while(i < len(s)):
            while s[j] != "-":
                j += 1
            number = int(s[i:j])
            ret_lst.append(s[j+1:j+1+number])
            i = j+1+number
            j=i
        return ret_lst

