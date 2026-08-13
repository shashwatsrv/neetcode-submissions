class Solution:
    #bottom-up
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False

        dp=set()
        dp.add(0)
        t=sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            nextdp=set()
            for x in dp:
                if (x+nums[i])==t:
                    return True
                nextdp.add(nums[i]+x)
                nextdp.add(x)
            dp=nextdp
        return True if t in dp else False

