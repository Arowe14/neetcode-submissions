class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [float("inf")] * (amount + 1)
        count[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    count[i] = min(count[i], 1 + count[i - coin])

        return count[amount] if count[amount] != float("inf") else -1