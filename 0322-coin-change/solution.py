class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1)
        coins.sort()
        for i in range(1,amount+1):
            m=float("inf")
            for j in coins:
                if i-j<0:
                    break
                m=min(dp[i-j]+1,m)
            dp[i]=m
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1


