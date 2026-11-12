class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mincost= prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<mincost:
                mincost=prices[i]
            elif prices[i]-mincost>profit:
                profit=prices[i]-mincost
        return profit