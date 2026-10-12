class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) == 0 or len(prices) == 1):
            return 0 
        min1 = prices[0]
        profitMax = 0
        for x in range(0,len(prices)):
            min1 = min(prices[x],min1)
            profitMax = max(prices[x]-min1,profitMax)
            print(min1)


        return profitMax


