class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = {} # Keys: (i, buying) val = max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in p:
                return p[(i, buying)]
            
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                p[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cooldown = dfs(i + 1, False)
                p[(i, buying)] = max(sell, cooldown)
            return p[(i, buying)]
        
        return dfs(0, True)

        

