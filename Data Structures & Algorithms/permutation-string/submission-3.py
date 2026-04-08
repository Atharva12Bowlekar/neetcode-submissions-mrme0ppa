class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        l = len(s1)
        c2 = Counter(s2[0:l])

        for i in range(l, len(s2)):
            if c2 == c1:
                return True
            c2[s2[i]] = c2.get(s2[i], 0) + 1
            c2[s2[i-l]] = c2.get(s2[i-l]) - 1
            
        return c2 == c1

        