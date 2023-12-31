class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while (i < len(prices) - 1):

            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            while (i < len(prices) - 1 and prices[i] <= prices[i + 1]):
                i += 1

            peak = prices[i]
            maxprofit += peak - valley
            
        return maxprofit

if __name__ == "__main__":
    prices = [3,2,6,5,0,3]
    s = Solution()

    print(s.maxProfit(prices))
