class Solution(object):
    def maxProfit(self, prices):
        buy=float('+inf')
        profit=0
        for x in prices:
            if x < buy:
                buy=x
            else:
                profit=max(profit,x-buy)
        return profit
