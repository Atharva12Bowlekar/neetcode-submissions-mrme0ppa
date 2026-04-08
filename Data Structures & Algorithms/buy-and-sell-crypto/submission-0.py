class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b = 0, 1
        profit = 0
        while b < len(prices):
            if prices[b] < prices[a]:
                a += 1
                b = a + 1
            else:
                profit = max(prices[b]-prices[a], profit)
                b += 1  
        return profit

        