class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dummy=nums[0]

        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        slowloop=0                
        while True:
            slowloop=nums[slowloop]
            slow=nums[slow]
            if slowloop==slow:
                return slow
            

        