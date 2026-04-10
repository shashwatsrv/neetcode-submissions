class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        cache=[-1]*n

        def topup(i):
            if i>=n:
                return 0
            if cache[i]!=-1:
                return cache[i]
            cache[i]=cost[i]+min(topup(i+1),topup(i+2))
            return cache[i]
        return min(topup(0),topup(1))