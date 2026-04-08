class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l = len(s1)

        for i in range(len(s2)- l+1):
            c2 = Counter(s2[i:i+l])
            print(c2)
            if c2 == c1:
                return True
        
        return False

        