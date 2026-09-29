class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #When two identical numbers are XORed, they cancel out, resulting in zero. Since every number appears twice except for one, the XOR of the entire array gives the number that appears only once. 
        ans=0
        for i in nums:
            ans^=i

        return ans