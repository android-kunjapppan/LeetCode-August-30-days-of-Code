class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstbuy, firstsell = float('-inf'),0
        secondbuy,secondsell = float('-inf'),0
        for price in prices:
            firstbuy = max(firstbuy,-price)
            firstsell = max(firstsell, firstbuy+price)
            secondbuy = max(secondbuy,firstsell - price)
            secondsell = max(secondsell,secondbuy+price)
        
        return secondsell
