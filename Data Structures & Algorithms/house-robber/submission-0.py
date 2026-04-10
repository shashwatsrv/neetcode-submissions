class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        cache=[-1]*n

        def robber(i):
            if i>=n:
                return 0
            if cache[i]!=-1:
                return cache[i]
            
            cache[i]=max(nums[i]+robber(i+2),robber(i+1))
            return cache[i]
        
        return robber(0)        

        