class Solution:
    def finding(self, piles, h, i):
        import math

        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/i)

        if total_hours <= h:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while r >= l:
            mid = (l + r)//2

            if self.finding(piles, h, mid) is True:
                if mid-1 == 0 or self.finding(piles, h, mid - 1) is False:
                    return mid
                else:
                    r = mid - 1
            else:
                l = mid + 1
