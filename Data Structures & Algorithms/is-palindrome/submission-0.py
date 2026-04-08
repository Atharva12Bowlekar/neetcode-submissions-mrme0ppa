class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                new_s += char
            else:
                pass
        new_s = new_s.lower()
        return new_s==new_s[::-1]
        