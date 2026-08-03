class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p=0
        c=0
        for i in range(2,len(cost)+1):
            p,c=c,min(cost[i-2]+p,cost[i-1]+c)
        return c
